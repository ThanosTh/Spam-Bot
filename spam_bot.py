# IMPORTS
import pyautogui, time

# VARIABLES
t = 1

# INPUTS
text = input('What sentence or word you want to spam:\n')
times = input('How many times do you want to spam it (e.g. 20):\n')
wait = input('How much time do you want the bot to wait between the spams (in seconds. At least 1):\n')

# COUNT DOWN
input('*****PRESS ENTER TO START*****')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
print('**********SPAM**********')

# SPAM LOOP
while t <= int(times):
	pyautogui.typewrite(text)
	pyautogui.press("enter")
	t += 1
	time.sleep(int(wait))