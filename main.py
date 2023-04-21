import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twitter import TwitterBot
import datetime

email='erick-pirata2@hotmail.com'
senha='Erick1@3$5'


class Velocidade():
    
    def obter_velocidade(self):
        
        driver=webdriver.Chrome()
        driver.get('https://fast.com/pt/')
        time.sleep(10)

        go_button = driver.find_element(By.ID,"speed-value")
        print(f'Sua internet está em {go_button.text}MB')
        self.velocidade = int(go_button.text)
            

internet=Velocidade()
internet.obter_velocidade()

if internet.velocidade < 500:
    twittar=TwitterBot(email, senha)
    twittar.login()
    twittar.reclamar()
