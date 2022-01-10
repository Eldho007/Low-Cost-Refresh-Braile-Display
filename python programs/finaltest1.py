import urllib
from PIL import Image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np
from nanpy import(ArduinoApi, SerialManager)
from time import sleep
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.IN, pull_up_down=gpio.PUD_UP)
dirPin1=3
stepsPin1=4
dirPin2=11
stepsPin2=9
src_path = "/home/pi/Documents/"
try:
    connection = SerialManager()
    a=ArduinoApi(connection = connection)
except:
    print("Failure")
def get_string(img_path):

    # Read image with opencv
    img = cv2.imread(img_path)
    #Rescaling the image
    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + "removed_noise.png", img)

    # Apply threshold to get image with only black and white
    img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "removed_noise.png"))

    # os.remove(temp)
    return result

print ("--- Start recognize text from image ---")
string = (get_string(src_path + "inferno1.png"))
print (string)
print ("------ Done -------")
length=len(string)
a.pinMode(dirPin1,a.OUTPUT)
a.pinMode(stepsPin1,a.OUTPUT)
a.pinMode(stepsPin2,a.OUTPUT)
a.pinMode(dirPin2,a.OUTPUT)
try:
    c=0
    while (c<length):
        button=gpio.input(21)
        sleep(0.5)
        if button==False:
         if(string[c]=='A' or string[c]=='a'):   
          a.digitalWrite(dirPin1,a.HIGH)
          a.digitalWrite(dirPin2, a.HIGH)
          a1=0
          a2=0
          while (a1<120):
             a.digitalWrite(stepsPin1, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             sleep(0.0001)
             a1=a1+1
          while (a2<0):
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             a2=a2+1
          sleep(5)
          a.digitalWrite(dirPin1,a.LOW);
          a.digitalWrite(dirPin2,a.LOW);
          a1=0
          a2=0
          while (a1<120):
             a.digitalWrite(stepsPin1, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             sleep(0.0001)
             a1=a1+1
          while (a2<0):
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             a2=a2+1
          sleep(1)
         if(string[c]=='B' or string[c]=='b'):   
          a.digitalWrite(dirPin1,a.HIGH)
          a.digitalWrite(dirPin2, a.HIGH)
          a1=0
          a2=0
          while (a1<225):
             a.digitalWrite(stepsPin1, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             sleep(0.0001)
             a1=a1+1
          while (a2<0):
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             a2=a2+1
          sleep(5)
          a.digitalWrite(dirPin1,a.LOW);
          a.digitalWrite(dirPin2,a.LOW);
          a1=0
          a2=0
          while (a1<225):
             a.digitalWrite(stepsPin1, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             sleep(0.0001)
             a1=a1+1
          while (a2<0):
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             a2=a2+1
             sleep(1)
         if (string[c] == 'C' or string[c] == 'c'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'D' or string[c] == 'd'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'E' or string[c] == 'e'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 120):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'F' or string[c] == 'f'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'G' or string[c] == 'g'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'h' or string[c] == 'H'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 225):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'I' or string[c] == 'i'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'J' or string[c] == 'j'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'K' or string[c] == 'k'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <0):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 0):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'L' or string[c] == 'l'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <0):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 <200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 0):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'M' or string[c] == 'm'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'N' or string[c] == 'n'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'O' or string[c] == 'o'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'P' or string[c] == 'p'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'Q' or string[c] == 'q'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'R' or string[c] == 'r'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 55):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'S' or string[c] == 's'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 175):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 175):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 120):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'T' or string[c] == 't'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 175):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 175):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 225):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'U' or string[c] == 'u'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <35):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 35):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'V' or string[c] == 'v'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <35):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 200):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 35):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'W' or string[c] == 'w'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <200):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 55):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 200):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'X' or string[c] == 'x'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <75):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 75):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'Y' or string[c] == 'y'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <200):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 200):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         if (string[c] == 'Z' or string[c] == 'z'):
             a.digitalWrite(dirPin1, a.HIGH)
             a.digitalWrite(dirPin2, a.HIGH)
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 <175):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(5)
             a.digitalWrite(dirPin1, a.LOW);
             a.digitalWrite(dirPin2, a.LOW);
             a1 = 0
             a2 = 0
             while (a1 < 75):
                 a.digitalWrite(stepsPin1, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin1, a.LOW)
                 sleep(0.0001)
                 a1 = a1 + 1
             while (a2 < 175):
                 a.digitalWrite(stepsPin2, a.HIGH)
                 sleep(0.0001)
                 a.digitalWrite(stepsPin2, a.LOW)
                 sleep(0.0001)
                 a2 = a2 + 1
             sleep(1)
         else:
          a.digitalWrite(stepsPin1, a.LOW)
          a.digitalWrite(stepsPin2, a.LOW)   
         c=c+1  
except:
        a.digitalWrite(stepsPin1, a.LOW)
        a.digitalWrite(stepsPin2, a.LOW)