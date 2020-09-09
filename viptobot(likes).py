from selenium import webdriver
import time
from colorama import init, Fore, Style, Back
from random import randint
init()

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Sending Likes!')

print(Fore.RED + ' ________      ________      ________      ___          ')
print(Fore.RED + '|\   ____\    |\   __  \    |\   __  \    |\  \         ')
print(Fore.RED + '\ \  \___|    \ \  \|\  \   \ \  \|\  \   \ \  \        ')
print(Fore.RED + ' \ \  \        \ \  \|\  \   \ \  \|\  \   \ \  \       ')
print(Fore.RED + '  \ \  \____    \ \  \|\  \   \ \  \|\  \   \ \  \____  ')
print(Fore.RED + '   \ \_______\   \ \_______\   \ \_______\   \ \_______\ ')
print(Fore.RED + '    \|_______|    \|_______|    \|_______|    \|_______|')
print('\n')
username = input("Video URL: ")
print(username + " is the selected video link")
def confirmF():
    confirm = input("Confirm? Y/N: ")
    if confirm == "Y":
        return
    else: quit()
confirmF()
print("Please complete the captcha")
time.sleep(1)
print("You will have 10 seconds to complete it")
time.sleep(2)
driver = webdriver.Chrome()
driver.get('https://vipto.de/')
time.sleep(10)
driver.minimize_window()
def initialize():
    time.sleep(5)
    heartsclick = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div/div[2]/div/button")
    heartsclick.click()
    heartstype = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div/input")
    heartstype.send_keys(username)
    search = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div/div/button")
    search.click()
    time.sleep(3)
    sendhearts = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/div/div[1]/div/form/button")
    sendhearts.click()
    t = (randint(150,152))
    countdown(int(t))
    driver.get('https://vipto.de/')
for _ in range(1,1000):
    initialize()
