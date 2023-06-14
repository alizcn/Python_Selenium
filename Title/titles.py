from selenium import webdriver
from selenium.webdriver.edge.service import Service

s = Service("exemsedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get("https://www.apple.com/")

driver.maximize_window()
link = driver.current_url
baslik = driver.title
print("sayfa başlığı : " + baslik)
if "apple.com" in link:
    print("Doğru Apple Sayfası : " + link)
driver.get("https://www.etsy.com/")
link = driver.current_url
baslik = driver.title
print("Başlık : " + baslik)
driver.save_screenshot("C:/Users/Ali/Desktop/etsy.png")
if "etsy.com" in link:
    print("Doğru Etsy Sayfası : " + link)
driver.back()
baslik=driver.title
driver.save_screenshot("C:/Users/Ali/Desktop/deneme.png")
if "Apple" in baslik:
    print("Tebrikler Apple sayfasına döndünüz")


driver.quit()