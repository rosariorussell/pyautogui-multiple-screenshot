import pyautogui
pyautogui.PAUSE = 0.2

arr = ['first_screenshot','second_screenshot','third_screenshot']

for x in arr:
  pyautogui.screenshot(f'{x}.png',region=(149,194,803,803))
  pyautogui.click(850,81)
  
  # print(pyautogui.KEYBOARD_KEYS)
# print(pyautogui.position())
# pyautogui.hotkey('ctrl','prtsc')
# pyautogui.typewrite("Hello World!")
# pyautogui.click(850,81)
