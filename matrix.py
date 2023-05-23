import cv2 as cv
from numpy import array
im_1 = cv.imread(r"tree.jpg")
ar = array(im_1)
print(ar)