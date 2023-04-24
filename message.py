import pyautogui
import time 
time.sleep(10)
for i in range(10):
    pyautogui.typewrite("hi "+str(i+1))
    pyautogui.press("enter")
