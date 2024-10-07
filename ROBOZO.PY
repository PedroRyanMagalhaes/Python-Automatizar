import pyautogui

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

pyautogui.press('enter')
pyautogui.write("Hello World")
