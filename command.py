import RPi.GPIO as GPIO
import time
import os
import subprocess
import json

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

data = {}
data['volume'] = '5'
data['status'] = 'stoped'


with open('state.txt', 'w') as outfile:
    json.dump(data, outfile)

while True:
        input_state17=GPIO.input(17)
        input_state27=GPIO.input(27)
        input_state22=GPIO.input(22)
        input_state18=GPIO.input(18)
        input_state23=GPIO.input(23)
        if input_state17==True:
                print('Scan Button Pressed 17')
                subprocess.call(['python','player.py'])
        if input_state27==True:
                print('Scan Button Pressed 27')
                subprocess.call(['python','pause.py'])
        if input_state22==True:
                print('Scan Button Pressed 22')
                subprocess.call(['python','next.py'])
        if input_state18==True:
                print('Scan Button Pressed 18')
                subprocess.call(['python','volume_up.py'])
        if input_state23==True:
                print('Scan Button Pressed 23')
                subprocess.call(['python','volume_down.py'])

