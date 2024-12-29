import cv2
import numpy as np
from utils import get_Limits
from PIL import Image
# Définir la couleur bleue en BGR
blue = [0, 255, 255]

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_Limits(color=blue)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    box = mask_.getbbox()
    if box is not None:
        x1, y1, x2, y2 = box
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()