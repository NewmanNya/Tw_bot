# 调试代码
# from  selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# client = webdriver.Chrome(chrome_options=chrome_options,executable_path='/usr/bin/twitter/chromedriver')
# client.get("https://www.google.com")
# content = client.page_source.encode('utf-8')
# print (content)
# client.quit()

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup as bs
import time

def init_driver():
    # initiate the driver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')



    # set a default wait time for the browser [5 seconds here]:
    driver.wait = WebDriverWait(driver, 5)

    return driver


def close_driver(driver):
    driver.close()

    return


def login_twitter(driver, username, password):
    # open the web page in the browser:
    driver.get("https://twitter.com/login")

    # find the boxes for username and password
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    # enter your username:
    username_field.send_keys(username)
    time.sleep(1)

    # enter your password:
    password_field.send_keys(password)
    time.sleep(1)

    # click the "Log In" button:
    driver.find_element_by_class_name("EdgeButtom--medium").click()
    print("Login in")

    return

def tweet(driver, string, picPath,picName):
    time.sleep(1)

    textInputEle=driver.find_element_by_name('tweet')
    textInputEle.send_keys(string)
    # picInputEle=driver.find_element_by_name('media_empty')
    # # picSend=os.path.join(picPath,picName)
    # picInputEle.send_keys(picPath+picName)
    time.sleep(5)
    driver.find_element_by_css_selector("button.tweet-action").click()

    print("Send tweet")



if __name__ == "__main__":
    # start a driver for a web browser:
    driver = init_driver()
    # UN  and PW
    username ="BotTamako"
    password ="2bd2c9434b974dc4953f0724be1b3f44d13bddfd08cdaa52b2105524fca42558"
    print("Start login")
    login_twitter(driver, username, password)
    print("Start tweet")
    tweet(driver, "test",'D:\\',"bg.jpg")

    #close_driver(driver)