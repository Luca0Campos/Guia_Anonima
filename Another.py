
from selenium import webdriver
import time

for navegador in range(1):

    #object of ChromeOptions class
    c = webdriver.ChromeOptions()

    #incognito parameter passed
    c.add_argument("--incognito")

    #set chromedriver.exe path
    navegador = webdriver.Chrome(executable_path="C:\\Drivers_Browsers\\chromedriver", options=c)
    navegador.implicitly_wait(0.5)
    navegador.maximize_window()

    #launch URL
    navegador.get("https://www.uol.com.br")
    time.sleep(5)


    navegador.close()
