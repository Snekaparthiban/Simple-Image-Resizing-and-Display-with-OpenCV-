
import cv2
import imutils
img=cv2.imread('dor.png')

resizedImg=imutils.resize(img,width=100)
cv2.imshow('OriginalImage2.jpg',img)
cv2.imshow('resized.jpg',resizedImg)
cv2.imwrite('resizedImage2.jpg',resizedImg)
cv2.waitKey(10000)
cv2.destroyAllWindows()
