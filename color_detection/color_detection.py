import cv2
import numpy as np
from utils import get_Limits

blue = [150,255,255]

capture = cv2.VideoCapture(0)
while True:
    ret,frame = capture.read()
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit = get_Limits(color=blue)
    mask = cv2.inRange(hsvImage,lowerLimit,upperLimit)
    cv2.imshow('frame',mask)

    if cv2.waitKey(1) != 27: # Escape
        break
capture.release()