import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11,gpio.OUT)
    gpio.setup(12,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)
    
def forward(tf):
    init()
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(11,True)
    gpio.output(12,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    init()
    gpio.output(11,True)
    gpio.output(12,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    init()
    gpio.output(11,True)
    gpio.output(12,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_right(tf):
    init()
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
reverse(0.8)

forward(0.8)