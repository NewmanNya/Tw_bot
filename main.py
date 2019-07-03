#Raw code for test
# from  selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# client = webdriver.Chrome(chrome_options=chrome_options,executable_path='/usr/bin/twitter/chromedriver')
# client.get("https://www.google.com")
# content = client.page_source.encode('utf-8')
# print (content)
# client.quit()

#First code
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
    # driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/usr/bin/twitter/chromedriver')
    # set a default wait time for the browser [5 seconds here]:
    driver.wait = WebDriverWait(driver, 5)
    
    return driver


def close_driver(driver):
    driver.close()

    return


def login_twitter(driver, username, password):
    driver.get("https://www.twitter.com")
    # open the web page in the browser:
    el = driver.find_element_by_css_selector('button.Button.js-login')
    el.click()
# fill out the username
    el = driver.find_element_by_css_selector("input.email-input")
# "type" in your screen name
    el.send_keys(username)
# fill out your password...again, another reason to use the API (with OAuth) and NOT
# your browser. At the very least, don't hardcode your password into the script

# "type" in your password
    driver.find_element_by_css_selector(".LoginForm-password > input").send_keys(password)
# Submit the form
    el.submit()
    print("Login in")

    return

def tweet_pic(driver, string, picPath, picName):
    time.sleep(1)
    textInputEle=driver.find_element_by_name('tweet')
    textInputEle.send_keys(string)
    picInputEle=driver.find_element_by_name('media_empty')
    # picSend=os.path.join(picPath,picName)
    picInputEle.send_keys(picPath+picName)
    time.sleep(5)
    driver.find_element_by_css_selector("button.tweet-action").click()
    print("Send tweet")
    
def tweet_text(driver, string):
    time.sleep(1)
    textInputEle=driver.find_element_by_name('tweet')
    textInputEle.send_keys(string)
    time.sleep(5)
    driver.find_element_by_css_selector("button.tweet-action").click()
    print("Send tweet")


if __name__ == "__main__":
    # start a driver for a web browser:
    driver = init_driver()
    # UN  and PW
    username ="BotTamako"
    f = open("pw.txt","r")   
    str = f.read()     
    f.close()  
    password =str
    print("Start login")
    login_twitter(driver, username, password)
    print("Start tweet")
    tweet_text(driver, "test")
    close_driver(driver)
