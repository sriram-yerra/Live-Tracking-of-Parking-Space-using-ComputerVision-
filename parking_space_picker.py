import cv2
# print("OpenCV version:", cv2.__version__)

import pickle
# pickle is a built-in Python module that lets you save Python objects to a file and load them back later — in other words, 
# it lets you serialize and deserialize Python objects.

img = cv2.imread("/home/sriram/Documents/Live-Tracking-of-Parking-Space-using-ComputerVision-/carParkImg.png")

width, height = 107, 48

posList = []

def mouseClick(events, x, y, flags, params):
    # if 18:32
    

while True:

    # cv2.rectangle(img, (51, 145), (158, 193), (0, 255, 0), 2)
    cv2.imshow("parking Image", img)

    cv2.setMouseCallback("parking Image", mouseClick)

    cv2.waitKey(0)
    # cv2.destroyAllWindows()



























































