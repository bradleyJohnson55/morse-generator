import time
import RPi.GPIO as gpio

# set your positive output GPIO pin here
OUT_PIN = 12

gpio.setmode(gpio.BCM)
gpio.setup(OUT_PIN, gpio.OUT)
gpio.setwarnings(False)


UNIT = 0.08
morseAlphabet = {"a": "01", "b": "1000", "c": "1010", "d": "100", "e": "0", "f": "0010", "g": "110", 
"h": "0000", "i": "00", "j": "0111", "k": "101", "l": "0100", "m": "11", "n": "10", "o": "111", "p": "0110", "q": "1101", 
"r": "010", "s": "000", "t": "1", "u": "001", "v": "0001", "w": "011", "x": "1001", "y": "1011", "z": "1100" }
str = ""

def callLetter(letter):
    if (letter == " "):
        time.sleep(7 * UNIT)
    else:
        for i in morseAlphabet[letter]:
            if int(i) == 0:
                gpio.output(OUT_PIN, 1)
                time.sleep(UNIT)
                gpio.output(OUT_PIN, 0)
                time.sleep(UNIT)
           
            elif int(i) == 1:
                gpio.output(OUT_PIN, 1)
                time.sleep(UNIT * 3)
                gpio.output(OUT_PIN, 0)
                time.sleep(UNIT)
           
        time.sleep(UNIT * 3)

while(str != "!no"):
    for i in str:
        callLetter(i)

    str = raw_input("Enter a word (or type \'!no\' to exit):\n")


