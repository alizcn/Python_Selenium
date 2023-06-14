import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s = Service("exemsedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("test")
driver.find_element(By.ID,"password").send_keys("asdf")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
mesaj=driver.find_element(By.ID,"flash").text


if "Your username is invalid!" in mesaj:
    print("OK,yanlış kullanıcı adı doğru çalışıyor")
else:
    print("HATA: yanlış kullanıcı adı çalışmıyor")

driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("asdf")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
mesaj2=driver.find_element(By.ID,"flash").text

if "Your password is invalid!" in mesaj2:
    print("OK,yanlış şifre doğru çalışıyor")
else:
    print("HATA: yanlış şifre çalışmıyor")
driver.find_element(By.ID,"username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,"button.radius").click()
mesaj3=driver.find_element(By.ID,"flash").text

if "You logged into a secure area!" in mesaj3:
    print("OK,doğru bilgiler kullanıcı adı doğru çalışıyor")
else:
    print("HATA: doğru bilgiler çalışmıyor")

link=driver.current_url
if "secure" in link:
    print("OK link secure içeriyor")
else:
    print("HATA:Link secure içermiyor")

dogru_mesaj=driver.find_element(By.CSS_SELECTOR,"div h2").text
if "Secure Area" in dogru_mesaj:
    print("Ok,Sayfa başlığı doğru")
else:
    print("HATA:sayfa başlığı yanlış")

driver.find_element(By.XPATH,"//i[contains(text(),'Logout')]").click()

if "login" in driver.current_url:
    print("OK,login sayfasına döndük")
else:
    print("HATA:login sayfasına dönmedi")

driver.quit()