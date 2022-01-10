import urllib
from nanpy import(ArduinoApi, SerialManager)
from time import sleep
dirPin1=3
stepsPin1=4
steps=40
dirPin2=11
stepsPin2=10
try:
    connection = SerialManager()
    a=ArduinoApi(connection = connection)
except:
    print("Failure")
a.pinMode(dirPin1,a.OUTPUT)
a.pinMode(stepsPin1,a.OUTPUT)
a.pinMode(stepsPin2,a.OUTPUT)
a.pinMode(dirPin2,a.OUTPUT)
try:
          a.digitalWrite(dirPin1,a.HIGH)
          a.digitalWrite(dirPin2, a.HIGH)
          z=0
          while (z<steps):
             a.digitalWrite(stepsPin1, a.HIGH)
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             z=z+1
          sleep(1)
          a.digitalWrite(dirPin1,a.LOW);
          a.digitalWrite(dirPin2,a.LOW);
          z=0
          while (z<steps):
             a.digitalWrite(stepsPin1, a.HIGH)
             a.digitalWrite(stepsPin2, a.HIGH)
             sleep(0.0001)
             a.digitalWrite(stepsPin1, a.LOW)
             a.digitalWrite(stepsPin2, a.LOW)
             sleep(0.0001)
             z=z+1
          sleep(1)
except:
        a.digitalWrite(stepsPin1, a.LOW)
        a.digitalWrite(stepsPin2, a.LOW)
 
