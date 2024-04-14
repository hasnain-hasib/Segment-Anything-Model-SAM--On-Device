# Image Segmentation with Segment Anything

This repository contains a simple Python script that performs image segmentation using the Segment Anything library. It segments objects in an input image and overlays the segmentation masks on the original image.

## Installation

To use this script, you'll need Python installed on your system. You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

Make sure you have the `segment_anything` library installed. You can install it via pip:

```
pip install segment-anything
```

## Usage

1. Place the input image(s) you want to segment in the same directory as the script.
2. Run the script using Python:

```
python segment_image.py
```

By default, the segmented image(s) will be saved in the same directory with filenames prefixed with "segmented_".

You can also specify the input image path and output image path as command-line arguments:

```
python segment_image.py input_image.jpg output_image.jpg
```

## Example

Here's an example of how to use the script:

```python
python segment_image.py input_image.jpg output_image.jpg
```

This will segment the objects in `input_image.jpg` and save the segmented image as `output_image.jpg`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
