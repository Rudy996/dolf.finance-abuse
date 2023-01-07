from multiprocessing import Pool
from random import choice
import time
from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")


refki = 3



f = open('mail.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("mail.txt", "r") as f:
    mail = f.read().split('\n')
    i = i - 1


def work(mail):
    try:
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        driver.get("http://dolf.finance/?referralcode=40YNGV") # реф-ка
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[3]/div/div/div/div/form/div/input"))).send_keys(mail)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[3]/div/div/div/div/form/div/div/button"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "number-form-control"))).click()
        ref = driver.find_element(By.ID, "copyInput").get_attribute("value")
        for x in range(refki):
            t = Thread(target=abuz, args=[ref])
            t.start()
            time.sleep(0.1)
        t.join()
        print(f"Аккаунт {mail} заабужена")

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def abuz(ref):
    try:
        rr = "https://" + ref
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        driver.get(rr)
        fake_mail = "".join([choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(8)]) + "@gmail.com"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[3]/div/div/div/div/form/div/input"))).send_keys(fake_mail)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='root']/div[3]/div/div/div/div/form/div/div/button"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "number-form-control"))).click()
        print("Register")
        time.sleep(1)
    except:
        pass

if __name__ == '__main__':
    p = Pool(processes=1) # кол-во потоков
    p.map(work, mail)