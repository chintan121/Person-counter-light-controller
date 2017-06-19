#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = [11,12,13,15,16,18,22,7]
photodiod =[31,32]
led=29

def sta():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(led, 0)
        
        for pd in photodiod:
                GPIO.setup(pd, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        
        for pin in pins:
                GPIO.setup(pin, GPIO.OUT) 
                GPIO.output(pin, GPIO.LOW)

def start():
        while True:
                j=0
                while True:
                        a=1
                        
                        if GPIO.input(31) == GPIO.HIGH:
                                while a==1:
                                        if GPIO.input(32) == GPIO.HIGH:
                                                j+=1
                                                a+=1
                                                time.sleep(1)
                        elif GPIO.input(32) == GPIO.HIGH:
                                while a==1:
                                        if GPIO.input(31) == GPIO.HIGH:
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
                        elif j==6:
                                GPIO.output(11,1)  
                                GPIO.output(12,0)  
                                GPIO.output(13,1)  
                                GPIO.output(15,1)
                                GPIO.output(led, 1)
                        
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
