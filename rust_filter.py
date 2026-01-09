import cv2
import numpy as np
import os
import glob

# This model acompany with rust detection algorithm

count = 0 #for counting the image has been preprocessed

def rust_detect(file):
        # read image
        A = cv2.imread(file)
        
        # image scaling
        scale_percent = 100
        width = int(A.shape[1] * scale_percent / 100)
        height = int(A.shape[0] * scale_percent / 100)
        dsize = (width, height)

        # resize image
        A = cv2.resize(A, dsize)
        
        # color converting BGR to HSV (Hue Saturation Value)
        img_hsv = cv2.cvtColor(A, cv2.COLOR_BGR2HSV)
        
        # Range for lower red
        lower_red = np.array([0,70,70])
        upper_red = np.array([20,255,150]) # [20,255,150] [20,200,150]
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
        
        # range for upper red
        lower_red = np.array([220,70,70]) # [220, 70, 70] [170,70,70]
        upper_red = np.array([255,255,150]) # [255, 255, 150] [180,200,150]
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
        
        # add both masks
        mask = mask0 + mask1
        
        output_img = cv2.bitwise_and(A ,A ,mask=mask)
        
        print("\n\n\n Number of pixels depicting rust \n >> %d"%(np.sum(mask)/255))
        cv2.imshow('image1',output_img)
        cv2.imshow('image2',A)
        cv2.waitKey(0)
        cv2.imwrite('output_image%d.jpg'%count,output_img)
        cv2.imwrite('image%d.jpg'%count,A)
        cv2.destroyAllWindows()
        os.system("cls")

     
os.system("color 0a")
os.system("cls")

print(""" Welcome to the rust detection software!! 
 The software detects the rusted portion of metal
 and visualize the rust pixels for 
 comparitive analysis.\n\n""")
print("**********************************************")

images = glob.glob("rust_img_01.jpg")

for path in images:
	count += 1
	rust_detect(path)

input("\n PRESS CTRL + C TO EXIT ")

