# June 23

import pickle
import cvzone
import cv2
import numpy as np

cap = cv2.VideoCapture('carPark.mp4')

with open('CarParkPos', 'rb') as f:
# with open('/home/sriram/Documents/Live-Tracking-of-Parking-Space-using-ComputerVision-/CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def checkParkingSpace(imgPro):

    spacecount = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y+width, x:x+height]
        
        ## cv2.imshow('hi', imgCrop)
        # cv2.imshow(str(x*y), imgCrop) # fir making every image chunk unique.

        count = cv2.countNonZero(imgCrop)
        # used to count the number of white (non-zero) pixels in a binary image or image region.

        if count < 900:
            color = (255, 0, 0)
            thickness = 3
            spacecount += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
        cv2.putText(
            img,
            str(count),
            (x, y + height - 3),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            thickness
        )

        displayText = f"Free: {spacecount}/{len(posList)}"
        cvzone.putTextRect(
            img, 
            displayText, 
            (50, 50), 
            scale=2,
            thickness=5, 
            offset=20, 
            colorR=(0,0,0)
        )

        displayText = f"Red --> Occupied, Blue --> Free"
        cvzone.putTextRect(
            img, 
            displayText, 
            (400, 50), 
            scale=2,
            thickness=3, 
            offset=20, 
            colorR=(0, 0, 0)
        )

        cv2.imshow("finalImg", img)

        # cv2.rectangle(imgPro, pos, (pos[0]+width, pos[1]+height), (255, 255, 255), thickness)
        # cv2.imshow("Image", imgPro)



# Making the video to run for an infinite loop. 
while True:
    # To loop a video — restart it from the beginning when it reaches the end.
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        # This sets the current frame position back to 0, i.e., the start of the video.
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # success is a Boolean value, which tells whether a frame was succcessfully read or not
    success, img = cap.read()

    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgBlur = cv2.GaussianBlur(imgGrey, (1, 1), 1)
    # (5,5) is the kernel size (width, height) of the filter.
    # It must be an odd number (like 3, 5, 7, 9...), a larger kernel = more blur.
    # 4 --> sigma (Standard Deviation)

    imgThresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY_INV, 25, 16)
    # 255 --> white regions
    # To convert a blurred grayscale image (imgBlur) into a binary image — 
    # where each pixel is either black or white, 
    
    # This below line applies median blur to a binary (thresholded) image in OpenCV:
    imgThreshMedianBlur = cv2.medianBlur(imgThresh, 5) # --> 2nd parameter should be an odd number. 
    # To remove small noise (specks, dots, or jagged edges) from the binary 
    ## image imgThresh, while preserving the edges better than Gaussian blur.

    kernel = np.ones((5, 5), np.uint8)
    # This creates a 5×5 matrix of ones (data type: uint8).
    # # It acts as the structuring element (or mask) used by the dilation process.
    # # Larger kernel → stronger dilation.
    
    # cv2.dilate(), which is used to expand white regions in a binary image.
    # imgdilate = cv2.dilate(imgThreshMedianBlur, kernel, iterations = 1)
    imgdilate = cv2.dilate(imgThreshMedianBlur, kernel)
    # Helps to:
        #1 Fill small black holes/gaps inside white areas
        #2 Strengthen or connect lines or shapes
        #3 Make contours more solid
    # 'iterations' specifies how many times the dilation operation is applied to the image.
    # Each iteration expands the white regions further.

    checkParkingSpace(imgdilate)

    # Drawing the rectangle on the frame after the image chunks have been created
    # for pos in posList:
    #     cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)

    # cv2.imshow("Image", imgThresh)
    # cv2.imshow("Image", img)
    # cv2.imshow("Image", imgdilate)

    # cv2.waitKey(1)
    cv2.waitKey(10)