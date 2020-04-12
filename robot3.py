import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11,gpio.OUT)
    gpio.setup(12,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)
    
def forward(tf):
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    gpio.output(11,True)
    gpio.output(12,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    gpio.output(11,True)
    gpio.output(12,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,False)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    gpio.output(11,True)
    gpio.output(12,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_right(tf):
    gpio.output(11,False)
    gpio.output(12,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()
    
def key_input(event):
    init()
    print("key:",event.char)
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == "w":
        forward(sleep_time)
    elif key_press.lower() == "s":
        reverse(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "q":
        pivot_left(sleep_time)
    elif key_press.lower() == "e":
        pivot_right(sleep_time)
    else:
        gpio.cleanup()
        

command = tk.Tk()
command.bind("<KeyPress>",key_input)
command.mainloop()