
from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://www.instagram.com/")
time.sleep(3)

email = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
email.send_keys("**************") # Your instagram e-mail
time.sleep(2)

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("**************") # Your instagram password
time.sleep(2)

enter = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
enter.click()

time.sleep(7)

no = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
no.click()

time.sleep(7)


notNow = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
notNow.click()

time.sleep(6)

dm = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
dm.click()

time.sleep(7)



driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button").click()

time.sleep(3)

receiver = "******" # Instagram name of the person you want to message
who = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input")
who.send_keys(receiver)

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[1]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[2]/div/button").click()
time.sleep(2)

messageSend = "❤️" # Message that you want to send

a=0
while a < 10:
    messageBox = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    messageBox.send_keys(messageSend)
    time.sleep(1)
    send = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
    send.click()
    a += 1




time.sleep(3)
# driver.close()