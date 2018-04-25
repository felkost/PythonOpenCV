#Changing image format
import cv2
img = cv2.imread('img.jpg')
cv2.imwrite('output_img_png.png', img, [cv2.IMWRITE_PNG_COMPRESSION])
