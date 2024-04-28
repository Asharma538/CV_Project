import numpy as np
import cv2
# load image
img = cv2.imread("Images/image1.jpg")
# create window
cv2.namedWindow("IMG")

#set default values
red = 0
green = 0
blue = 0

# functions to set values
def setBlue(val):
        global blue
        blue = val-255
        colorShift()

def setGreen(val):
        global green
        green = val-255
        colorShift()

def setRed(val):
        global red
        red = val-255
        colorShift()

# function that performs the colorshift
def colorShift():
        # create working copy
        res = img.copy()

        # modify hue
        # converted layer to uint16 to accomodate values larger than 255
        blue_array = np.uint16(res[:,:,0])+blue
        # clip min and max values - prevents unwanted wrap around
        blue_array = np.where(blue_array > 255 , 255, blue_array)
        blue_array = np.where(blue_array < 0, 0, blue_array)
        # convert back to uint8 and assign to image layer
        res[:,:,0] = np.uint8(blue_array)

        # modify green  - same process 
        green_layer = np.uint16(res[:,:,1])+green
        green_layer = np.where(green_layer > 255 , 255, green_layer)
        green_layer = np.where(green_layer < 0, 0, green_layer)
        res[:,:,1] = np.uint8(green_layer)

        # modify red - same process 
        red_layer = np.uint16(res[:,:,2])+red
        red_layer = np.where(red_layer > 255 , 255, red_layer)
        red_layer = np.where(red_layer < 0, 0, red_layer)
        res[:,:,2] = np.uint8(red_layer)

        # display result
        cv2.imshow("IMG", res)


#create trackbars to modify values
cv2.createTrackbar("Blue","IMG",255,510,setBlue)
cv2.createTrackbar("Green","IMG",255,510,setGreen)
cv2.createTrackbar("Red","IMG",255,510,setRed)

# display initial image
cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()