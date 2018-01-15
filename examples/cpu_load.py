#!/usr/bin/env python

import math
from time import localtime, sleep

try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

from blinkt import set_pixel, set_brightness, clear, show

def show_graph(v):
    clear()
    v *= 8
    for x in range(8):

        if x < 6:
            r, g, b = 40, 127, 0
        if x > 5:
            r, g, b = 127, 0, 2
        if v  < 0:
            r, g, b = 0, 0, 0
            
        set_pixel(x, r, g, b)
        v -= 1

set_brightness(0.1)

while True:
    t = localtime()
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec
    
    v = psutil.cpu_percent() / 100.0
    show_graph(v)

    set_pixel(0, 40, 127, 0)

    # Blink LED 7 aqua
    if ((s % 2) > 0):
        set_pixel(0, 127, 80, 0)
    
    show()
    sleep(.1)
