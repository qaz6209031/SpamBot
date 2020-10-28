import pyautogui ,time
time.sleep(5)
f = open("ipman_movie_script", 'r')
for word in f:
   pyautogui.typewrite(word)
   pyautogui.press("enter")
