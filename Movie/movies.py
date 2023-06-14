import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


s = Service("exemsedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.maximize_window()

driver.get("https://www.imdb.com")
driver.find_element(By.ID,"imdbHeader-navDrawerOpen").click()
time.sleep(1)
#edge de xpath ile kopyala ve yapıştır,çalıştı
driver.find_element(By.XPATH,"//span[text()='Top 250 Movies']").click()
#elementS çoklu seçim--liste halinde döndürür
film_names=driver.find_elements(By.XPATH,"//table/tbody//tr//td[@class='titleColumn']")

for i in film_names:
    if i.text[-5:-1]=="2000":
        print(i.text)