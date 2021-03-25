import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
chan_list = [21,20,16,12,7,8,25,24]
GPIO.setup(chan_list, GPIO.OUT)

def lightUp(ledNumber, period):
    GPIO.output(ledNumber,1)
    time.sleep(period)
    GPIO.output(ledNumber,0)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (blinkCount):
        GPIO.output(ledNumber,1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber,0)
        time.sleep(blinkPeriod)   

def runningLight(count, period):
    for i in range (count):
        for j in range (8):
            lightUp(chan_list[j], period)

def runningDark(count, period):
    for i in range (8):
        GPIO.output(chan_list[i],1)
    for j in range (count):    
        for i in range (8):
                GPIO.output(chan_list[i],0)
                time.sleep(period)
                GPIO.output(chan_list[i],1)
    for i in range (8):
        GPIO.output(chan_list[i],0)  

def lightNumber(number):
    n = 7
    p=0
    x=[]
    while n>0:
        p=int(number/2**n)
        if p == 1:
            x.append(1)
            number-=2**n
        else:
            x.append(0)    
        n-=1
    x.append(number)
    
    m=[0]*8
    m=x
    for i in range (8):
        GPIO.output(chan_list[i], m[i])             

def decToBin(decNumber):
    n = 7
    p=0
    x=[]
    while n>0:
        p=int(decNumber/2**n)
        if p == 1:
            x.append(1)
            decNumber-=2**n
        else:
            x.append(0)    
        n-=1
    x.append(decNumber)
    print(x)
    


#lightUp(21,5)
#blink(7, 5, 1)
#runningLight(2,0.5)
#runningDark(2, 0.1)

#decToBin(3)
#lightNumber(10)

#GPIO.output(chan_list,0)

