__author__ = 'kanehiro'
import ev3dev.ev3 as ev3
from time import sleep
btn = ev3.Button()
sound = ev3.Sound()
while not btn.backspace:
    if btn.enter:
        sound.speak("Enter")
    if btn.up:
        sound.speak("Up")
    if btn.down:
        sound.speak("Down")
    if btn.left:
        sound.speak("Left")
    if btn.right:
        sound.speak("Right")
    sleep(0.1)
