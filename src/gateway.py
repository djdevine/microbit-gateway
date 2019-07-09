import microbit
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

SEND_RATE = 1.0

pink = "p"
yellow = "y"
blue = "b"
red = "r"
green = "g"
violet = "v"
white = "w"

def process_incoming(msg):
    print("rx:%s" % str(msg))
    message = msg[0]
    if message == pink:
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        print("p")
    elif message == blue:
        keyboard.press('b')
        time.sleep(0.1)
        keyboard.release('b')
        print("b")
    elif message == red:
        keyboard.press('r')
        time.sleep(0.1)
        keyboard.release('r')
        print("c")
    elif message == green:
        keyboard.press('g')
        time.sleep(0.1)
        keyboard.release('g')
        print("g")
    elif message == violet:
        keyboard.press('v')
        time.sleep(0.1)
        keyboard.release('v')
        print("v")
    elif message == white:
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.release('w')
        print("w")
    elif message == yellow:
        keyboard.press('y')
        time.sleep(0.1)
        keyboard.release('y')
        print("y")
    else:
        print("error")

print("gateway running")
microbit.send_message("ready\n")

while True:
    msg = microbit.get_next_message()
    if msg is not None:
        process_incoming(msg)