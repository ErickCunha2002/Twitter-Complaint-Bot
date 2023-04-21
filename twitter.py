import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

hoje=datetime.datetime.now()
minutos=hoje.minute
horas=hoje.hour


# Dados de login
email = 'erick-pirata2@hotmail.com'
senha = 'Erick1@3$5'

class TwitterBot():

    def __init__(self, email, senha): 
        self.email=email
        self.senha=senha
        self.driver = webdriver.Chrome()

    def login(self):
        
        # Abre o Twitter e clica no botão para realizar login.
        self.driver.get('https://twitter.com/')
        button_login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
        button_login.click()
        
        # Adiciona o email e clica em continuar.
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, 
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        email_input.send_keys(self.email)
        
        next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_step.click() 

        # Tenta realizar a confirmção, caso seja necessário.
        try:
            confirmar = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, 
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')))
            confirmar.send_keys('@Bronzi_lucas')
        except:
            print('Não houve necessidade de confirmação.')
        next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next_step.click() 
        
        # Espera o campo de senha ficar visível e digita a senha.
        password = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, 
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password.send_keys(self.senha)

        #Realiza o login.
        realizar_login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, 
             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')))
        realizar_login.click()
        
    def reclamar(self):
        
        self.login()
        
        # Clica no botão de twittar
        button_twitter = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, 
        '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')))
        button_twitter.click()
            
        # Adiciona um comentário.
        comentario = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, 
        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')))
        comentario.send_keys(f'Hoje, às {horas}h, minha internet está uma porcaria, Desktop internet!')        
        time.sleep(2)
        
        # Envia a mensagem.
        enviar_msg = self.driver.find_element(By.XPATH, 
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        enviar_msg.click()

        time.sleep(2)
        self.driver.quit()

