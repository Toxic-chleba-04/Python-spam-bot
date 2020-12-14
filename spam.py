import pyautogui
from time import sleep
import time

sleep(3)

msg = input("Enter the message: ")
n = input("How many times ? : ")

sleep(3)

for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')


