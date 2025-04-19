import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

link = 'https://www.instagram.com/?flo=true'
browser = webdriver.Chrome()
browser.get(link)
time.sleep(5)

user_name = 'YourUsername'
pass_word = 'YourPassword'

user_ip = browser.find_elements(By.XPATH,".//input[@class='_aa4b _add6 _ac4d _ap35']")[0]
user_ip.click()
user_ip.send_keys(user_name)

pass_ip = browser.find_elements(By.XPATH,".//input[@class='_aa4b _add6 _ac4d _ap35']")[1]
pass_ip.click()
pass_ip.send_keys(pass_word)

login_button = browser.find_element(By.XPATH,"//button[@class=' _acan _acap _acas _aj1- _ap30' ]")
login_button.click()

#class
save_info = browser.find_element(By.XPATH,"//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37']")
save_info.click()
time.sleep(5)

#class
profile_logo = browser.find_elements(By.XPATH,"//div[@class='x1n2onr6 x6s0dn4 x78zum5']")
profile_logo[10].click()

followers_div = browser.find_elements(By.XPATH,"//li[@class='xl565be x1m39q7l x1uw6ca5 x2pgyrj']")
list_of_followers = followers_div[1]
list_of_followers.click()
time.sleep(3)

followers_popup = browser.find_element(By.XPATH,"//div[@class='x1ja2u2z x1afcbsf x1a2a7pz x6ikm8r x10wlt62 x71s49j x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6']")

followers_set = set()


scroll_box = followers_popup.find_element(By.XPATH,".//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")

last_height = 0
while True:
    
    users = scroll_box.find_elements(By.XPATH,"//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
    # print(len(users))
    for user in users:
        try:
            username = user.find_element(By.XPATH,".//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']").text
            followers_set.add(username)
        except:
            continue

    # Scroll down
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
    time.sleep(4)  

    new_height = browser.execute_script("return arguments[0].scrollTop", scroll_box)
    if new_height == last_height:
        break
    last_height = new_height


followers_list = list(followers_set)
print(f"Total followers: {len(followers_list)}")

close_btn = browser.find_element(By.XPATH,".//div[@class='_abm0' ] ")
close_btn.click()

following_div = browser.find_elements(By.XPATH,"//li[@class='xl565be x1m39q7l x1uw6ca5 x2pgyrj']")
list_of_following = following_div[2]
list_of_following.click()
time.sleep(3)

following_popup = browser.find_element(By.XPATH,"//div[@class='x1ja2u2z x1afcbsf x1a2a7pz x6ikm8r x10wlt62 x71s49j x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6']")

following_set = set()


scroll_box = following_popup.find_element(By.XPATH,".//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")

last_height = 0
while True:
   
    users = scroll_box.find_elements(By.XPATH,"//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
    # print(len(users))
    for user in users:
        try:
            username = user.find_element(By.XPATH,".//span[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']").text
            following_set.add(username)
        except:
            continue

    # Scroll down
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
    time.sleep(5)  

   
    new_height = browser.execute_script("return arguments[0].scrollTop", scroll_box)
    if new_height == last_height:
        break
    last_height = new_height


following_list = list(following_set)
print(f"Total following: {len(following_list)}")

unfollowers = following_set - followers_set
unfollowers_list = list(unfollowers)
print(len(unfollowers_list))
for it in unfollowers_list:
    print(it)