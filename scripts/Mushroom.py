import threading
import keyboard as kb
import time as t
import win32api, win32con
import random
from ..HPapi import check_lobby

current_lobby = {"data2": "", "data3": ""}

def update_lobby_data():
    global current_lobby
    while not kb.is_pressed('`'):
        data = check_lobby()
        current_lobby["data2"] = data[2].lower()
        current_lobby["data3"] = data[3].lower()
        t.sleep(0.5)

def move():
    RT1 = 0.1
    RT2 = 0.2
    directions = [
        ('s', 96),
        ('w', 99),
        ('a', 0.1)
    ]

    for key, duration in directions:
        kb.press(key)
        start_time = t.time()
        while t.time() - start_time < duration:
            if current_lobby["data2"] != "skyblock" or current_lobby["data3"] != "garden":
                kb.release(key)
                return False
            t.sleep(0.5)
        kb.release(key)

    return True

def cycle():
    t.sleep(0.5 + random.uniform(0.1, 0.2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    for _ in range(5):
        if not move():
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            return

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def warp():
    t.sleep(0.3)
    kb.press_and_release('/')
    t.sleep(0.1 + random.uniform(0.1, 0.2))
    string = 'warp garden'
    kb.write(string)
    kb.press_and_release('enter')
    t.sleep(0.1 + random.uniform(0.1, 0.2))
    kb.press_and_release('1')
    t.sleep(3 + random.uniform(0.1, 0.2))
    kb.press('shift')
    t.sleep(0.5 + random.uniform(0.1, 0.2))
    kb.release('shift')

def playSB():
    t.sleep(0.3)
    kb.press_and_release('/')
    t.sleep(0.1 + random.uniform(0.1, 0.2))
    kb.press_and_release('l')
    t.sleep(0.1 + random.uniform(0.1, 0.2))
    kb.press_and_release('enter')
    t.sleep(3)
    kb.press_and_release('/')
    t.sleep(0.1 + random.uniform(0.1, 0.2))
    string = 'play skyblock'
    kb.write(string)
    kb.press_and_release('enter')

if __name__ == '__main__':
    lobby_thread = threading.Thread(target=update_lobby_data, daemon=True)
    lobby_thread.start()

    t.sleep(3)
    while not kb.is_pressed('`'):
        if current_lobby["data2"] != "skyblock" or current_lobby["data3"] != "garden":
            t.sleep(5)
            playSB()
            t.sleep(5)
            warp()
        else:
            warp()
            cycle()