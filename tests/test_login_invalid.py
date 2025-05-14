from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Proje dizininizde bulunan chromedriver dosyasının yolunu belirtin
service = Service("./chromedriver.exe")  # Windows için: "./chromedriver.exe"

# WebDriver'ı başlatın
driver = webdriver.Chrome(service=service)

try:
    # Login sayfasına git
    driver.get("https://the-internet.herokuapp.com/login")

    # Yanlış kullanıcı adı ve şifre gir
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("wronguser")
    password_input.send_keys("wrongpass")
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Sayfanın yüklenmesini bekle

    # Hata mesajını kontrol et
    error_message = driver.find_element(By.ID, "flash").text
    if "Your username is invalid!" in error_message:
        print("✅ Test Başarılı: Hata mesajı göründü.")
    else:
        print("❌ Test Başarısız: Hata mesajı bulunamadı.")

finally:
    # Tarayıcıyı kapat
    driver.quit()
