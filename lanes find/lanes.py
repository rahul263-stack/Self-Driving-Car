# MOTIVE FIND THE AREA OF INTEREST
import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(lane_image):
    grey = cv2.cvtColor(lane_image, cv2.COLOR_RGB2BGR)
    # blurring the image to reduce the noise
    blur = cv2.GaussianBlur(grey, (5, 5), 0)
    # here it will outline the final border
    kanny = cv2.Canny(blur, 50, 150)
    return kanny


def region_of_interest(image):
    height = image.shape[0]
    polygon = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

def display_lines(img, lines):
        line_image = np.zeros_like(img)
        if lines is not None:
                for line in lines:
                        x1, y1, x2, y2 = line.reshape(4)
                        cv2.line(line_image,(x1,y1), (x2,y2), (255,0,0),10)
                        return line_image

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = canny(lane_image)
interest = region_of_interest(canny)
mixed_image = cv2.addWeighted(lane_image,0.8,lane_image,1,1)
lines = cv2.HoughLinesP(mixed_, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

line_image =display_lines(lane_image,lines)
cv2.imshow('result', line_image)


cv2.waitKey(0)

"""
# CODE TO CONVERT IMAGE INTO GRAYSCALE ->  to reduce the complexity from rgb to only black and white
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2BGR)
cv2.imshow("result", gray)
cv2.waitKey(0)"""

# -> REDUCING THE NOISE --  because it will create additional edges hence we will smoothing the image
"""
image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2BGR)
blur = cv2.GaussianBlur(gray, (5,5 ), 0)
cv2.imshow("result", blur)
cv2.waitKey(0)
"""

# -> DiSPLAYING LINES OVER THE OTHER PICTURE
"""
def display_lines( image ,lines):
        line_image = np.zeros_like(image)
        if lines in lines:
                x1, y1 ,x2, y2 = line.reshape(4)
                cv2.line(line_image, (x1,y1),(x2,y2), (255,0,0), 10)
        return line_image 
"""
