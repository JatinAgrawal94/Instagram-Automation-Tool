#script for automating Like,Comment feature on Instagram using selenium webdriver

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys 
import time
import emoji

firefoxOptions = Options()
# firefoxOptions.add_argument("-headless")
# install needed web borwser driver at path './drivers/driver_name'
# here we have used geckodriver
browser = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefoxOptions)
browser.maximize_window()
browser.get('https://instagram.com')
time.sleep(5)

#login page elements
username=browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
login_button=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

#Assigning values to login page elements
#replace string by respective username and password
username.send_keys('username')
password.send_keys('password')
login_button.click()
time.sleep(5)

# getting the profile page of a instagram account
profilepage=browser.get('https://www.instagram.com/mercedesbenz/')

time.sleep(4)
browser.execute_script("window.scrollTo(0,200)")
time.sleep(4)

#main process
for i in range(1,4):
    post=browser.find_element_by_xpath('html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[%s]/a/div/div[2]'%i)
    post.click()
    time.sleep(7)
    like_button=lambda: browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span').click()
    like_button()
    time.sleep(2)
    comment_section=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
    comment_section.click()
    comment_section=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
    comment_section.send_keys(emoji.emojize("Nice Car :red_heart:",variant="emoji_type"))
    time.sleep(2)
    post_button=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
    post_button.click()
    time.sleep(7)
    exit_button=browser.find_element_by_xpath('/html/body/div[5]/div[3]/button');
    exit_button.click()
    time.sleep(3)

browser.execute_script("window.scrollTo(0,0)")