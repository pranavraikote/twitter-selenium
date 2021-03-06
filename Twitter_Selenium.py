#Import modules
from selenium import webdriver
import time

#Import the Chrome driver, use the absolute path
driver = webdriver.Chrome("C:\\Users\\Pranav\\Downloads\\chromedriver_win32\\chromedriver.exe")

#Open the website
driver.get("https://twitter.com/login")

#Take screenshots
#driver.get_screenshot_as_file("C:\\Users\\Pranav\\Downloads\\T1.png")

#Find the user-name and password elements
username = driver.find_element_by_class_name("js-username-field")
password = driver.find_element_by_class_name("js-password-field")

#Maximize the browser window
driver.maximize_window()

#Fill the text fields
username.send_keys('<<username>>') #Replace with username
password.send_keys('<<password>>') #Replace with password 


#Login-button
driver.find_element_by_class_name("EdgeButtom--medium").click()

#time.sleep(30)
driver.set_page_load_timeout(30)

#Take screenshots
#driver.get_screenshot_as_file("C:\\Users\\Pranav\\Downloads\\T2.png")

#Click on the tweet button
driver.find_element_by_class_name("js-global-new-tweet").click()


#Find tweetbox
post=driver.find_element_by_xpath("//*[@id='Tweetstorm-tweet-box-0']/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]")

#The tweet content
post.send_keys("Hi There, Fullly automated tweet using python")

#Send tweet
driver.find_element_by_class_name("SendTweetsButton ").click()
time.sleep(10)

#Log-out safely
driver.find_element_by_class_name("js-dropdown-toggle").click()
driver.find_element_by_id("signout-button").click()

#Close the session 
driver.close()
driver.quit()
                                                                                                         
