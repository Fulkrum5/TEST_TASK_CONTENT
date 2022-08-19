from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#Открытие браузера в полный экран
link =  "https://xn--d1abb2a.xn--p1ai/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[1]/nav/a[1]")))
#Регистрация
reg_choice = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[1]/nav/a[1]")
reg_choice.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[1]/input")))
reg_name = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[1]/input")
reg_name.send_keys("Автотест")
reg_phone = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[2]/input")
reg_phone.send_keys("89126000068")
reg_mail = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[3]/input")
reg_mail.send_keys("zahar.ershov1@gmail.com")
reg_password = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[4]/input")
reg_password.send_keys("TestPassword33990")
reg_button = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[3]/div/button")
reg_button.click()
#ввести код и нажать энтер необходимо самостоятельно. Без апи провести данные действия в автоматическом режиме не получится

