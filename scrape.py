#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import wget
import os
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
dl_path = config['DEFAULT']['OUTPUT']
user = config['DEFAULT']['USERNAME']
secret = config['DEFAULT']['SECRET']
page_photo_link = "https://www.facebook.com/pg/TwinklingDreamsWeddingPlanners/photos/?ref=page_internal"
if not os.path.exists(dl_path):
       print("path doesn't exist. trying to make")
       os.makedirs(dl_path)
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get('http://www.facebook.com')
driver.execute_script("window.alert = function() {};")
try:
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    submit = driver.find_element_by_id("u_0_2")
except NoSuchElementException as err:
    submit = driver.find_element_by_id("u_0_8")
    print("[-]Error:{0}".format(err))
username.send_keys(user)
password.send_keys(secret)
time.sleep(5)
submit.submit()
time.sleep(10)
driver.get(page_photo_link)
time.sleep(5)
try:
    for i in range(8):
        print("[+]Scroll loop:",i)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
except NoSuchElementException as err:
    print("[-]Error:{0}".format(err))
a_href = []
try:
    for image in driver.find_elements_by_class_name('_2eea'):
        href = image.find_element_by_xpath('.//a[1]').get_attribute("href")
        a_href.append(href)
        print("[+]Text:",href)
except NoSuchElementException as err:
    print("[-]Error:{0}".format(err))
try:
    for h in a_href:
        driver.get(h)
        time.sleep(5)
        src = driver.find_element_by_class_name("spotlight").get_attribute("src")
        print("Image source:",src)
        wget.download(src, dl_path)
        time.sleep(5)
except NoSuchElementException as err:
    print("[-]Error:{0}".format(err))
time.sleep(10)
driver.quit()
