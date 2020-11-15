import network
import time
from machine import Pin


net = network.WLAN(network.STA_IF)
net.active(True)
net.connect('your-ssid', 'your-password')
led_g = Pin(14, Pin.OUT)
led_y = Pin(12, Pin.OUT)
led_r = Pin(13, Pin.OUT)


def led(y=0, r=0, g=0):
    """Set pin to 0(or 1) output level"""
    led_y(y)
    led_r(r)
    led_g(g)


while net:
    try:
        stat = net.status('rssi')
        time.sleep(0.5)
        if stat >= -60:
            led(0, 0, 1)
        elif stat > -75 and stat <= -61:
            led(1, 0, 0)
        else:
            led(0, 1, 0)
    except:
        break
