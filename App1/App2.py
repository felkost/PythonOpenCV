#Loading and saving an gray image 
import cv2
gray_img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', gray_img)
cv2.imwrite('output_img.jpg', gray_img)
cv2.waitKey()
