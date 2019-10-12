import time
from selenium import webdriver

with open('p1','r') as f:
    nums = f.read().splitlines()
login = nums[0]
password = nums[1]

driver = webdriver.Chrome(executable_path = 'C:/TEMP/DYAKOVA/web/chromedriver.exe')

driver.get('https://github.com/login')

input_login = driver.find_element_by_name('login')
input_login.send_keys(login)

input_password = driver.find_element_by_name('password')
input_password.send_keys(password)

input_click = driver.find_element_by_name('commit')
input_click.click()
---------------------------------------
import time
from selenium import webdriver

with open('p1','r') as f:
    nums = f.read().splitlines()
login = nums[0]
password = nums[1]

driver = webdriver.Chrome(executable_path = 'C:/TEMP/DYAKOVA/web/chromedriver.exe')

driver.get('https://www.nstu.ru/')

in_link = driver.find_element_by_css_selector('a.header__login-link')
in_link.click()








