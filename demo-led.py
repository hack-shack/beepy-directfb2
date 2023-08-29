#!/usr/bin/python
"""
Copyright (c) 2023 Asa Durkee. MIT License.
Demonstrates beepy RGB LED.
"""
import os
import time

led_power = "/sys/firmware/beepy/led"
led_red   = "/sys/firmware/beepy/led_red"
led_green = "/sys/firmware/beepy/led_green"
led_blue  = "/sys/firmware/beepy/led_blue"
keyboard_backlight = "/sys/firmware/beepy/keyboard_backlight"

breathe_delay = 0.1    # 1.000 = 1 second. 0.001 = 1ms.

def main():
    with open(led_power,mode='w') as p:
        p.write('1')
    leds_to_illuminate = [led_red, led_green, led_blue, keyboard_backlight]
    for led in leds_to_illuminate:
        breathe(led)

def breathe(led_to_illuminate):
    breathe_levels = [0,10,30,60,100,120,160,200,225,255]
    for level in breathe_levels:
        with open(led_to_illuminate,mode='w') as r:
            r.write(str(level))
        time.sleep(breathe_delay)
    for level in reversed(breathe_levels):
        with open(led_to_illuminate,mode='w') as r:
            r.write(str(level))
        time.sleep(breathe_delay)

# MAIN
# =========================================================
uid = os.geteuid()
print("INFO : UID is: " + str(uid))
if os.geteuid() == 0:
    print("INFO : Script is running as root. This is expected behavior.")
if os.geteuid() != 0:
        exit("ERROR: You need to run this script with sudo, or as the root user.")

if __name__ == "__main__":
    main()