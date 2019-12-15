#!/usr/bin/env python3

    # This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
    # be installed and it is strongly recommended that you use the latest
    # release of Raspbian.

import subprocess
import time
import os
import board
import digitalio

print("press a button!") #used for testing

#Define our button selection- 5 buttons for station choices:

#First Button 
button1 = digitalio.DigitalInOut(board.D24)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#Second Button
button2 = digitalio.DigitalInOut(board.D23)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

#Third Button 
button3 = digitalio.DigitalInOut(board.D5)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

#Fourth Button
button4 = digitalio.DigitalInOut(board.D17)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

#Fifth button
button5 = digitalio.DigitalInOut(board.D22)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

#A poor mans pause button in case of awful sound
button6 = digitalio.DigitalInOut(board.D27)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP

#A shutdown button
button = digitalio.DigitalInOut(board.D3)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.UP

while True:

     if not button1.value:
        subprocess.call(['killall', 'mpg123'])
        print("stopped previous track")
        os.system('mpg123 -q http://east-mp3-128.streamthejazzgroove.com/ &')
        print ("playing jazz groove")

     if not button2.value:
        print("stopped previous track")
        subprocess.call(['killall', 'mpg123'])
        os.system('mpg123 -q http://server1.chilltrax.com:9000/ &')
        print ("playing chilltrax")
        
     if not button3.value:
        subprocess.call(['killall', 'mpg123'])
        print("stopped previous track")
        os.system('mpg123 -q http://lb.zenfm.be/zenfm.mp3 &')
        print ("playing zenfm")

     if not button4.value:
        subprocess.call(['killall', 'mpg123'])
        print("stopped previous track")
        os.system('mpg123 -q http://ice2.somafm.com/christmas-256-mp3 &')
        print("playing SomaFM Christmas")

     if not button5.value:
        subprocess.call(['killall', 'mpg123'])
        print("stopped previous track")
        os.system('mpg123 -q http://ice1.somafm.com/groovesalad-256-mp3 &')
        print ("playing groove salad")

     if not button6.value:  #stop playing music
        subprocess.call(['killall', 'mpg123'])
        print("music paused - press button to continue")
        
     if not button7.value:  #put the pi to sleep
        subprocess.call(['shutdown', '-h', 'now'], shell=False)  

time.sleep(.25)


