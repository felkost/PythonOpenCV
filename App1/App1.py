#Reading, displaying images 
import cv2
img = cv2.imread('img.jpg')
cv2.imshow('Input image', img)
cv2.waitKey()