import numpy as np
import cv2 as cv
img = cv.imread('/home/ai3/Desktop/common/ML/Day10/Questions/apple.jpg')
rows,cols,_ = img.shape
M = np.float32([[1,0,200],[0,1,100]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
