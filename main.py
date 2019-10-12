import time
from selenium import webdriver

with open('p1','r') as f:
    nums = f.read().splitlines()
login = nums[0]
password = nums[1]

driver = webdriver.Chrome(executable_path = 'C:/TEMP/DYAKOVA/web/chromedriver.exe')

driver.get('https://login.nstu.ru/ssoservice/XUI/#login/&goto=http%3A%2F%2Fciu.nstu.ru%2Fstudent_study%2F')

time.sleep(15)

input_login = driver.find_element_by_name('callback_0')
input_login.send_keys(login)

input_password = driver.find_element_by_name('callback_1')
input_password.send_keys(password)

time.sleep(5)

input_click = driver.find_element_by_name('callback_2')
input_click.click()













