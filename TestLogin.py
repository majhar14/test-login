from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
path = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.homedepot.com/auth/view/signin?redirect=/&ref=null")

try:
    login_page_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    login_page_email.send_keys("farhi86@yahoo.com")


    login_page_pass = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password-input-field"))
    )
    login_page_pass.send_keys("XXXXXXXX")


    login_page_button = driver.find_element_by_class_name("bttn__content")
    login_page_button.click()
    print(driver.title)

except Exception:
    time.sleep(60)
    driver.quit()

