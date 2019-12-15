
    # This script requires a Raspberry Pi 2, 3 or Zero. Circuit Python must
    # be installed and it is strongly recommended that you use the latest
    # release of Raspbian.
import subprocess
import time
import os
import board
import digitalio

print("press a button!")

button1 = digitalio.DigitalInOut(board.D24)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D23)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D5)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

button4 = digitalio.DigitalInOut(board.D17)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

button5 = digitalio.DigitalInOut(board.D22)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.UP

button6 = digitalio.DigitalInOut(board.D7)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.UP



while True:

        # omxplayer -o local <file>
        # omxplayer -o hdmi <file>
        # omxplayer -o both <file>
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

     if not button6.value:
        subprocess.call(['killall', 'mpg123'])
        print("music paused - press button to continue")

time.sleep(.25)


