from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Launch Home Page

path = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.hudl.com/login")

# Login credentials

try :

  login_page_email = driver.find_element_by_id("email")
  login_page_email.send_keys("majhar14@gmail.com")
  login_page_passwoord = driver.find_element_by_id("password")
  login_page_passwoord.send_keys("xxxxxxxx")
  login_button = driver.find_element_by_id("logIn")
  login_button.click()
  time.sleep(10)
  driver.close()

except Exception : 
  print ("Login Fail")


