from neopixel import NeoPixel
from machine import Pin
from vgkits.color import *

pixels = None

RGB = (0, 1, 2, 3)
GRB = (1, 0, 2, 3)
RBG = (0, 2, 1, 3)
PL9823 = RGB
WS2811 = GRB
WS2812 = WS2811


def startPixels(pin=None, num=None, order=None):
    global pixels
    if pin is None:
        pin = Pin(14)
    if num is None:
        num = 8
    if order is None:
        NeoPixel.ORDER = WS2811
    pixels = NeoPixel(pin, num)
    return pixels


def setPixel(index, color, show=True):
    pixels[index] = color
    if show:
        pixels.write()


def showPixels():
    pixels.write()


def clearPixels(indexes=None, color=black, show=True):
    if indexes == None:
        indexes = range(pixels.n)
    for index in indexes:
        setPixel(index, color, False)
    if show:
        showPixels()

if __name__ == "__main__":
    startPixels()
    clearPixels()
