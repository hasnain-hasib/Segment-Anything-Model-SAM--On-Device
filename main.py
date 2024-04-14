import cv2
import numpy as np
import os
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator

def segment_image(input_image_path, output_image_path=None):
    if not os.path.isfile(input_image_path):
        print(f"Error: Input image '{input_image_path}' not found.")
        return None

    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Error: Failed to read image at '{input_image_path}'.")
        return None

    sam_checkpoint = "sam_vit_b_01ec64.pth"
    model_type = "vit_b"
    device = "cpu"
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)

    mask_generator = SamAutomaticMaskGenerator(
        model=sam,
        points_per_side=32,
        pred_iou_thresh=0.9,
        stability_score_thresh=0.96,
        crop_n_layers=1,
        crop_n_points_downscale_factor=2,
        min_mask_region_area=100
    )
    masks = mask_generator.generate(image)

    for mask in masks:
        image = cv2.addWeighted(image, 0.8, (mask['segmentation'] * 255).astype(np.uint8), 0.2, 0)

    if output_image_path is None:
        output_image_path = os.path.join(os.path.dirname(input_image_path), "segmented_" + os.path.basename(input_image_path))

    cv2.imwrite(output_image_path, image)

    print(f"Segmented image saved at: {output_image_path}")
    return output_image_path

input_image_path = "seg.jpg"
segment_image(input_image_path)
