import pyautogui, time
time.sleep(3)
f = open('D:/Thanos/Desktop/spam bot/spam_test_text.txt', 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
	time.sleep(3)
