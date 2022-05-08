import cv2
import numpy as np

img = cv2.imread('data/frame115.png', cv2.IMREAD_COLOR)

p1 = [670, 730]
p2 = [1350, 720]
p3 = [350, 940]
p4 = [1650, 920]

actual = np.float32([p1, p2, p3, p4])

width, height = 1630, 1630

p1w = [0, 0]
p2w = [width, 0]
p3w = [0, height]
p4w = [width, height]

warped = np.float32([p1w, p2w, p3w, p4w])

M = cv2.getPerspectiveTransform(actual, warped)
wimg = cv2.warpPerspective(img, M, (width, height))

filename = 'data/output.png'
cv2.imwrite(filename, wimg)
