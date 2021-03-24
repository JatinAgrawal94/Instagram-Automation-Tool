from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

firefoxOptions = Options()
browser = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefoxOptions)
browser.maximize_window()

browser.get('https://instagram.com')
time.sleep(5)

#login page elements
username=browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
login_button=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

#Assigning values to login page elements
username.send_keys('jatin.18becem069@gmail.com')
password.send_keys('jatingoestousa')
login_button.click()
time.sleep(3)

# post page
browser.get('https://www.instagram.com/p/CMlp_SMhVcl/?utm_source=ig_web_copy_link')
time.sleep(2)

#/html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul
# post_comments=browser.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul')
# post_comments_text=browser.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul').text
# browser.execute_script('arguments[0].scrollIntoView(false)',post_comments) 
search_string='//html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul'+'[1]'
comment_array=[]

for i in range(1,4): 
    s='//html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul['+str(i)+']'
    comment_array.append(s)
    
i=0
try:
    while(1):
        post_comments=browser.find_element_by_xpath(comment_array[i])
        post_comments_text=browser.find_element_by_xpath(comment_array[i]).text
        browser.execute_script('arguments[0].scrollIntoView(false)',post_comments)
        post_comments_text=browser.find_element_by_xpath(comment_array[i]).text
        print(post_comments_text)
        i+=1
except:
    print("Exception occured")
        
        
# post_comments_text=browser.find_element_by_xpath('//html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul/ul').text
# print(post_comments_text)

# /html/body/div[1]/section/main/div/div[1]/article/div[3]/div[1]/ul
# post_comments_tag=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[1]/div/li')
# post_comments=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[1]/div/li').text
# print(post_comments)

# browser.execute_script('arguments[0].scrollIntoView();', post_comments_tag)
# post_comments=browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[1]/div/li').text
# print(post_comments)