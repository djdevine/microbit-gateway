import microbit
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()

SEND_RATE = 1.0

def process_incoming(msg):
    print("rx:%s" % str(msg))
    if str(msg) == "MB1:A":
        keyboard.press(Key.left)
        time.sleep(0.2)
        keyboard.release(Key.left)
        print("left")
    elif str(msg) == "MB1:B":
        keyboard.press(Key.right)
        time.sleep(0.2)
        keyboard.release(Key.right)
        print("right")
    elif str(msg) == "MB1:S":
        keyboard.press(Key.up)
        time.sleep(0.3)
        keyboard.release(Key.up)
        print("up")
    #Add your incoming message processing here
    #any radio message sent by any microbit, will arrive here

def process_outgoing(msg):
    # Example of sending a message on a timer
    # Just call microbit.send_message whenever you have new data
    # this will be sent to the gateway micro:bit which will then
    # broadcast it to all listening micro:bit devices
    print("tx:%s" % str(msg))
    microbit.send_message(msg)

next_send = time.time() + SEND_RATE

print("gateway running")

count = 0
while True:
    msg = microbit.get_next_message()
    if msg is not None:
        process_incoming(msg)

    #now = time.time()
    #if now >= next_send:
    #   next_send = now + SEND_RATE
    #   process_outgoing(str(count))
    #   count = (count + 1) % 10
