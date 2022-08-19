from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Открытие браузера в полный экран
link =  "https://xn--d1abb2a.xn--p1ai/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
wait = WebDriverWait(browser, 5)
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[1]/nav/a[2]")))
#Аутентификация
auth_choice = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[1]/nav/a[2]")
auth_choice.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[1]/input")))
login = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[1]/input")
login.send_keys("70000000001")
password = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[1]/div[2]/input")
password.send_keys("test123456")
auth = browser.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div/form/div[2]/div/button")
auth.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div[2]/a[1]")))
#Создание новой поездки
travel_create = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div[2]/a[2]/div[2]")
travel_create.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[1]/div/input[2]")))
#Ввод пунктов отправления и назначения
departure = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[1]/div/input[2]")
departure.send_keys("Екатеринбург")
#sleep здесь необходим для разграничения инпута
time.sleep(1)
departure.send_keys(Keys.ENTER)
destination = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div/input[2]")
destination.send_keys("Пермь")
time.sleep(1)
destination.send_keys(Keys.ENTER)
departure_street = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[2]/div/input")
departure_street.send_keys("Белинского, 38")
destination_street = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[2]/div[2]/div/input")
destination_street = ("Советской Армии, 4")
next = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[3]/div/button")
next.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div/input[2]")))
#ввод времени отправления
departure_date = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div")
departure_date.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/div/div[2]/div[31]")))
departure_date_choice = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div/div[2]/div[31]")
departure_date_choice.click()
departure_time = browser.find_element(By.XPATH,"/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[2]/div")
departure_time.click()
#wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")))
next2 = browser.find_element(By.XPATH,"/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")
next2.click()
#ввод марки автомобиля

try:
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[1]/div/input[2]")))
    car_brand = browser.find_element(By.XPATH,"/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[1]/div/input[2]")
    car_brand.send_keys("Tesla")
    #дальнейшие sleep-ы сделаны для поддержания небольшого временного промежутка между инпутами
    time.sleep(1)
    car_brand.send_keys(Keys.ENTER)
    time.sleep(1)
    car_model = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[1]/div[2]/div/input[2]")
    time.sleep(1)
    car_model.send_keys("Model S")
    time.sleep(1)
    car_model.send_keys(Keys.ENTER)
    car_year = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/input")
    car_year.send_keys("2020")
    car_id =  browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/input")
    car_id.send_keys("A202AA")
    next3 = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")
    next3.click()
except:
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div/div/div[2]/div")))
    print("Машина уже существует")
    next3 = browser.find_element(By.XPATH,"/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")
    next3.click()

#Ввод дополнительной информации
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[4]/div/div[2]/textarea")))
comment = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[4]/div/div[2]/textarea")
comment.send_keys("Тестовое задание")
instant_order = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/div[3]/div/div/div[2]/label/span")
instant_order.click()
next4 = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[5]/div/button")
next4.click()
#Cумма и подтверждение
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")))
next5 = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")
next5.click()
#Метод оплаты
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div/div[1]/div/div[3]")))
cash = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[1]/div/div/div[1]/div/div[3]")
cash.click()
next6 = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/form/div/div[2]/div/button")
next6.click()
#Согласие на публикацию
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/div/form/div/div[2]/div/button")))
pay = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div[2]/div[1]/div/div/form/div/div[2]/div/button")
pay.click()
#Переход в меню водителя
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section/div/div/div/div/div/div/form/div[2]/button")))
user = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[1]/div[2]/div")
user.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[2]/div[2]/div[2]/nav[3]/div/a[1]")))
user_driver = browser.find_element(By.XPATH, "/html/body/div[2]/header/div/div/div[3]/div[2]/div[2]/div[2]/nav[3]/div/a[1]")
user_driver.click()
#Редакция поездки и ее удаление
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/a")))
travel_details = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div/div[2]/a")
travel_details.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div[1]/div/div[4]/div/div/a")))
travel_edit = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div[1]/div/div[4]/div/div/a")
travel_edit.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div/div/form/div/div[3]/button[2]")))
travel_delete = browser.find_element(By.XPATH, "/html/body/div[2]/main/section[2]/div/div/div/div/div/form/div/div[3]/button[2]")
travel_delete.click()
wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/form/div[2]/div[1]/div/button")))
delete_ok = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/form/div[2]/div[1]/div/button")
delete_ok.click()
time.sleep(3)
browser.close()