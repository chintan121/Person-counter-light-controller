#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = [11,12,13,15,16,18,22,7]
photodiod =[31,32]
led=29

def sta():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(led, 0)
        for pin in pins:
                GPIO.setup(pin, GPIO.OUT) 
                GPIO.output(pin, GPIO.LOW)

def pd1():
    bb=0
    GPIO.setup(31,GPIO.OUT)
    GPIO.output(31,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(31,GPIO.IN)
    while GPIO.input(31)==GPIO.LOW:
        bb+=1
        
    return bb
def pd2():
    bd=0
    GPIO.setup(32,GPIO.OUT)
    GPIO.output(32,GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(32,GPIO.IN)
    while GPIO.input(32)==GPIO.LOW:
        bd+=1
        
    return bd



def start():
        while True:
                j=0
                while True:
                        a=1
                        
                        if pd1()/100>26:
                                while a==1:
                                        if pd2()/100>26:
                                                j+=1
                                                a+=1
                                                time.sleep(1)
                        elif pd2()/100>26:
                                while a==1:
                                        if pd1()/100>26:
                                                j-=1
                                                a+=1
                                                time.sleep(1)
                        
                        elif j<0:
                                j=0
                
                        elif j==0:
                                GPIO.output(11,1)  
                                GPIO.output(12,1)  
                                GPIO.output(13,1)  
                                GPIO.output(15,1)  
                                GPIO.output(16,1)  
                                GPIO.output(18,1)  
                                GPIO.output(22,0)  
                                GPIO.output(7,0)
                                GPIO.output(led, 0)
                                print 0
                                
                        elif j==1:
                                GPIO.output(11,0)  
                                GPIO.output(12,1)  
                                GPIO.output(13,1)  
                                GPIO.output(15,0)  
                                GPIO.output(16,0)  
                                GPIO.output(18,0)
                                GPIO.output(led, 1)
                                GPIO.output(22,0)  
                                GPIO.output(7,0)
                                print 1
                        elif j==2:
                                GPIO.output(11,1)
                                GPIO.output(led, 1)
                                GPIO.output(12,1)  
                                GPIO.output(13,0)  
                                GPIO.output(15,1)  
                                GPIO.output(16,1)  
                                GPIO.output(18,0)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0)
                                print 2
                        elif j==3:
                                GPIO.output(11,1)  
                                GPIO.output(12,1)
                                GPIO.output(led, 1)
                                GPIO.output(13,1)  
                                GPIO.output(15,1)  
                                GPIO.output(16,0)  
                                GPIO.output(18,0)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0)
                                print 3
                        elif j==4:
                                GPIO.output(11,0)  
                                GPIO.output(12,1)  
                                GPIO.output(13,1)  
                                GPIO.output(15,0)  
                                GPIO.output(16,0)  
                                GPIO.output(18,1)  
                                GPIO.output(22,1)
                                GPIO.output(led, 1)
                                GPIO.output(7,0)
                                print 4
                        elif j==5:
                                GPIO.output(11,1)  
                                GPIO.output(12,0)  
                                GPIO.output(13,1)  
                                GPIO.output(15,1)  
                                GPIO.output(16,0)  
                                GPIO.output(18,1)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0)
                                GPIO.output(led, 1)
                                print 5
                        elif j==6:
                                GPIO.output(11,1)  
                                GPIO.output(12,0)  
                                GPIO.output(13,1)  
                                GPIO.output(15,1)
                                GPIO.output(led, 1)
                                print 6
                                GPIO.output(16,1)  
                                GPIO.output(18,1)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0) 
                        elif j==7:
                                GPIO.output(11,1)  
                                GPIO.output(12,1)  
                                GPIO.output(13,1)  
                                GPIO.output(15,0)
                                GPIO.output(led, 1)
                                GPIO.output(16,0)  
                                GPIO.output(18,0)  
                                GPIO.output(22,0)  
                                GPIO.output(7,0)
                                print 7
                        elif j==8:
                                GPIO.output(11,1)  
                                GPIO.output(12,1)  
                                GPIO.output(13,1)
                                GPIO.output(led, 1)
                                GPIO.output(15,1)  
                                GPIO.output(16,1)  
                                GPIO.output(18,1)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0)
                                print 8
                        elif j==9:
                                GPIO.output(11,1)  
                                GPIO.output(12,1)
                                GPIO.output(led, 1)
                                GPIO.output(13,1)  
                                GPIO.output(15,1)  
                                GPIO.output(16,0)  
                                GPIO.output(18,1)  
                                GPIO.output(22,1)  
                                GPIO.output(7,0)
                                print 9

                        elif j>9:
                                GPIO.output(11,0)  
                                GPIO.output(12,0)
                                GPIO.output(led, 1)
                                GPIO.output(13,0)  
                                GPIO.output(15,0)  
                                GPIO.output(16,0)  
                                GPIO.output(18,0)  
                                GPIO.output(22,0)  
                                GPIO.output(7,1) 
                                print 'cant display but will be counted'

                        
              

def end():
        for pin in pins:
                GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()          

if __name__ == '__main__':     
        sta()
        try:
                start()
        except KeyboardInterrupt:  
                end()
