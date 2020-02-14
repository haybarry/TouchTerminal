
from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import spidev
from time import sleep


# calibration parameters

calib_scale240 = 288   # Likely about 285
calib_scale320 = 391   # Likely about 384
calib_offset240 = 29   # Likely about 28
calib_offset320 = 27   # Likely about 25


# Raspberry Pi configuration.
PEN = 6

TFT = TFT24T(spidev.SpiDev(), GPIO)
# print(GPIO)
# Raw touch output is intrinsically portrait mode

TFT.initTOUCH(PEN)

while 1:
    while not TFT.penDown():
        pass
    # x = TFT.readValue(TFT.X)  # raw 12-bit coordinate from touchscreen device
    # y = TFT.readValue(TFT.Y)  # These 2 are for the penprint on display
    x = 0
    y = 0
    for i in range (0,10):
        x = x + TFT.readValue(TFT.X)  # raw 12-bit coordinate from touchscreen device
        y = y + TFT.readValue(TFT.Y)  # These 2 are for the penprint on display
    x = x/10
    y = y/10



    # penprint: find lcd coordinates (240x320) according to 4 scaling factors already at top of this file
    x2 = int((x) * calib_scale240 / 4096 - calib_offset240)
    y2 = int((4096 - y) * calib_scale320 / 4096 - calib_offset320)

    # print("%03X" % TFT.readValue(TFT.X))
    # print("%03X" % TFT.readValue(TFT.Y))
    print("%03d" % x2, " ",end = '')
    print("%03d" % y2)

    if (10 <= x2 <= 40):
        print("Row 1")
    elif (70 <= x2 <= 100):
        print("Row 2")
    elif (130 <= x2 <= 160):
        print("Row 3")
    elif (190 <= x2 <= 220):
        print("Row 4")

    if (275 <= y2 <= 305):
        print("Column 1")
    elif (211 <= y2 <= 241):
        print("Column 2")
    elif (147 <= y2 <= 177):
        print("Column 3")
    elif (83 <= y2 <= 113):
        print("Column 4")
    elif (19 <= y2 <= 49):
        print("Column 5")

    print("")
    sleep(.5)

    # if TFT.penDown():
    #     print("Pen Down")
    # else:
    #     print("Pen Up")

    # print(TFT.penDown())
    # print("")
    # sleep(.5)