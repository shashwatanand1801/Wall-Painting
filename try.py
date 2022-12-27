import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('pic.jpg')

image = cv2.resize(image, (960, 540))

# img = cv2.imread('pic.jpg')

# img = cv2.resize(img, (960, 540))




# cv2.imshow("Pic", img)

# cv2.waitKey(0)

# img_gaussian = []
# cv2.GaussianBlur(image, img_gaussian)


#robert
#prepare the x(horizontal) and y(vertical) kernel matrices
kernelRobertx = np.array([[1,0],[0,-1]])
kernelRoberty = np.array([[0,1],[-1,0]])
#apply x kernel
img_robertx = cv2.filter2D(image, -1, kernelRobertx)
#apply y kernel
img_roberty = cv2.filter2D(image, -1, kernelRoberty)
img_robert = img_robertx + img_roberty
#prewitt
#prepare the x(horizontal) and y(vertical) kernel matrices
kernelPrewittx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernelPrewitty = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
#apply x kernel
img_prewittx = cv2.filter2D(image, -1, kernelPrewittx)
#apply y kernel
img_prewitty = cv2.filter2D(image, -1, kernelPrewitty)
img_prewitt = img_prewittx + img_prewitty
#sobel
#apply x kernel
img_sobelx = cv2.Sobel(image,cv2.CV_8U,1,0,ksize=3)
#apply y kernel
img_sobely = cv2.Sobel(image,cv2.CV_8U,0,1,ksize=3)
img_sobel = img_sobelx + img_sobely
#canny
img_canny = cv2.Canny(image,400,600)
#laplacian of gaussian
img_laplacian = cv2.Laplacian(image,cv2.CV_64F)


# cv2.imshow("Prewitt", img_prewitt)

# cv2.imshow("Sobel", img_sobel)

cv2.imshow("Canny", img_canny)


img_canny = cv2.Canny(image,100,500)
cv2.imshow("Canny2", img_canny)



kernel = np.ones((5, 5), np.uint8)

# img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

cv2.imshow("Dilate", img_dilation)


# cv2.imshow("Laplacian",img_laplacian)

cv2.waitKey(0)