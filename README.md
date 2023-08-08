# Color Detection Algorithm using Python and OpenCV

![Color Detection Demo](demo.png)

## Introduction

This repository contains a Python script that demonstrates a color detection algorithm using the OpenCV library. The algorithm is designed to identify and isolate specific colors in an image or video stream, showcasing the relationship between the RGB (Red, Green, Blue) and HSV (Hue, Saturation, Value) color spaces.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Color Spaces](#color-spaces)
- [Algorithm](#algorithm)
- [Demo](#demo)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/your-username/color-detection.git

vbnet
Copy code

2. Navigate to the repository's directory:

cd color-detection

markdown
Copy code

3. Install the required dependencies:

pip install opencv-python

arduino
Copy code

## Usage

1. Place the image or video file you want to process in the same directory as the script.

2. Open the terminal and run the script:

python color_detection.py

vbnet
Copy code

3. The script will prompt you to enter the name of the image or video file.

4. Next, you'll be asked to provide the color you want to detect in the format "R G B" (e.g., "255 0 0" for red).

5. The script will display the original image alongside the color-detected output, allowing you to visually compare the results.

## Color Spaces

The script showcases the relationship between the RGB and HSV color spaces. RGB represents colors as a combination of red, green, and blue components, while HSV represents colors using hue, saturation, and value components. This relationship is utilized to make color detection more robust and flexible.

## Algorithm

The color detection algorithm follows these steps:

1. Load the image or video frame.
2. Convert the image to both RGB and HSV color spaces.
3. Define the lower and upper bounds of the target color in both RGB and HSV.
4. Create masks for the target color in both color spaces.
5. Apply the masks to the original image, highlighting the detected color.
6. Display the original image and the color-detected output side by side.

## Demo

![Color Detection Demo](demo.png)

The above demo image shows the input image on the left and the color-detected output on the right. The color-detected output highlights the detected color (in this case, red) while preserving the rest of the image in grayscale.

## License

This project is licensed under the MIT License, allowing you to modify and distribute the code for both personal and commercial purposes.

Feel free to contribute to this repository by opening issues or submitting pull requests. Your contributions are greatly appreciated!

---

Happy color detecting!

*Note: Images used in the demo are for illustration purposes only and are not included in the repository.*