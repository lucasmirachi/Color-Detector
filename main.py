import cv2
import imageio
from PIL import Image

from util import get_limits

#blue = [255, 0, 0]
#green = [0, 255, 0]
#red = [0, 0, 255]
yellow = [0, 255, 255]

# To use a video
video_path = './test.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# To use webcam
#cap = cv2.VideoCapture(0)

frames = []

while True:
    success, img = cap.read()

    #converting the image's BGR colorspace to HSV color space

    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    #creating a mask to gather all the pixels that belong to the color we want to detect
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    #drawing a bounding box around the color object
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 5)

    cv2.imshow('Image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

output_gif_path = 'output.gif'
imageio.mimsave(output_gif_path, frames, format='GIF', duration=0.1)

cv2.destroyAllWindows()
