from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Clicked!")

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(617,504)[0] < 10:
        click(617,504)
    if pyautogui.pixel(717,504)[0] < 10:
        click(717,504)
    if pyautogui.pixel(817,504)[0] < 10:
        click(817,504)
    if pyautogui.pixel(917,504)[0] < 10:
        click(917,504)
