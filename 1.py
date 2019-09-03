from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("path of chromedriver.exe") #path of the chrome driver
browser.get('https://www.google.com/')

search = browser.find_elements_by_css_selector("input[name=q]")
search[0].send_keys('facebook')

browser.get('https://www.facebook.com/')

username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys('manikumarvikas')

password = browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys('9573762293')

loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()

time.sleep(3)
browser.quit()
