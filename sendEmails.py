#!/usr/bin/python3.9
#sends emails using selenium webdriver
#
#Lots of time.sleep so everything can load
# selenium has built in (waiting to load) modules for the time thing
# but is a lot more than the book taught
# can update later if I comeback

# WARNING - dont forget to put a email account and password in the variables <--------


import time, pyinputplus as pypi
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# account info
email = '' #email address here
paswrd = '' # password to email address
# email info
address = pypi.inputEmail(prompt='\nWhat email are you sending to?\n\n')
subject = input('\nWhats the subject of the email?\n\n')
message = input('\nWhat message are you sending?\n\n')

# pulls up google
browser = webdriver.Chrome(executable_path='/home/jj1here/Downloads/chromedriver')
browser.get('https://google.com')

# clicks sign in
signInElem = browser.find_element_by_link_text('Sign in')
signInElem.click()
time.sleep(1)

# sends email username
emailElem = browser.find_element_by_xpath("//input[@type='email']")
emailElem.send_keys(email)

# clicks next
nextElem = browser.find_element_by_class_name('VfPpkd-LgbsSe')
nextElem.click()
time.sleep(1)

# enters password
passElem = browser.find_element_by_name("password")
passElem.click()
passElem.send_keys(paswrd)

# clicks next
nextElem = browser.find_element_by_class_name('VfPpkd-LgbsSe')
nextElem.click()
time.sleep(1)

# clicks gmail
gmailElem = browser.find_element_by_link_text('Gmail')
gmailElem.click()
time.sleep(3)

# clicks compose
composeElem = browser.find_element_by_css_selector('.T-I.T-I-KE.L3')
composeElem.click()
time.sleep(1)

# expands email interface
biggerElem = browser.find_element_by_css_selector('.Hq.aUG')
biggerElem.click()
time.sleep(1)

# enters email recipient
addressElem = browser.find_element_by_css_selector('.vO')
addressElem.click()
addressElem.send_keys(address)
addressElem.send_keys(Keys.ENTER) #to enter the recipients email
time.sleep(1)

# enters subject
subjectElem = browser.find_element_by_xpath("//input[@name='subjectbox']")
subjectElem.click()
subjectElem.send_keys(subject)
time.sleep(1)

# enters message
messageElem = browser.find_element_by_xpath('//div[@role="textbox"]')
messageElem.click()
messageElem.send_keys(message)
time.sleep(1)

# clicks sends
sendElem = browser.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
sendElem.click()


time.sleep(4)
#closes everything
browser.quit() 