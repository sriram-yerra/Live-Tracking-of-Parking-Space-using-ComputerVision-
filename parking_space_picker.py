# June 23

import cv2
# print("OpenCV version:", cv2.__version__)

import pickle
# pickle is a built-in Python module that lets you save Python objects to a file and load them back later — in other words, 
# it lets you serialize and deserialize Python objects.

# img = cv2.imread("/home/sriram/Documents/Live-Tracking-of-Parking-Space-using-ComputerVision-/carParkImg.png")

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
    # open the file named CarParkPos, rb --> read in binary mode

        posList = pickle.load(f)
        # This loads serialized data from the file using the pickle module.
        # Reads binary data from the object f.
        # Deserializes it into a Python object (in this case, likely a list) and assigns it to posList

except: # file not found, unpickling error, etc
    posList = []

# This is the callback functiIn Python (and programming in general), a callback is a function passed as an argument 
# to another function, so it can be called (invoked) later when something happens — usually in response to an event.
# on that gets called when the mouse is used inside that window.
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos

            x2 = x1 + width
            y2 = y1 + height

            if x1 < x < x2 and y1 < y < y2:
                posList.pop(i)
    
while True:
    # img = cv2.imread("/home/sriram/Documents/Live-Tracking-of-Parking-Space-using-ComputerVision-/carParkImg.png")
    img = cv2.imread('carParkImg.png')

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (0, 255, 0), 2)

    cv2.imshow("parking Image", img)

    # the title should be the same as the imshow (parking Image)
    cv2.setMouseCallback("parking Image", mouseClick)
    # 'mouseClick' is a callback function   
    # It tells OpenCV to listen for mouse events (like clicks) in a window and handle them with a function.

    cv2.waitKey(1)

    # cv2.destroyAllWindows()



























































