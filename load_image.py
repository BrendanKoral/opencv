import cv2
import numpy as np
import matplotlib.pyplot as plt

#Imports image, reads as grayscale
img = cv2.imread('laguna.jpg', cv2.IMREAD_GRAYSCALE)

"""
Other options:
#IMREAD_COLOR = 1, grayscale = 0
#IMREAD_UNCHANGED = -1
"""

#Displays image
cv2.imshow('image', img)
#Waits for any key to be pressed, closes all windows
cv2.waitKey(0)
cv2.destroyAllWindows()