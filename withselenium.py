import time
import pandas as pd # Ler o arquivo excel

# Automizar a web
from selenium import webdriver # Navegador
from selenium.webdriver.common.by import By # Achar os elementos
from selenium.webdriver.common.keys import Keys # Digitar no teclado da web


# 0 - Ler o arquivo Excel
arquivo = "teste.xlsx"
url = "https://docs.google.com/forms/d/e/1FAIpQLSfwDHPzx_gSxM7FP4yPWYybDJdqhJHhdpr6jKwdgoIW0BRh9w/viewform?vc=0&c=0&w=1&flr=0"

df = pd.read_excel(arquivo)

# 1 - Loopar cada linha do arquivo 
for index, row in df.iterrows():
    print("Index: " + str(index) + " E o nome do fulano é " + row["NOME"])
    
    #   1.1 - Preencher os dados lidos para cada linha no navegador web
    chrome = webdriver.Chrome(executable_path="chromedriver.exe")
    chrome.get(url)
    time.sleep(2)
    
    nome  = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    telefone = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    nome.send_keys(row["NOME"])
    telefone.send_keys(row["TELEFONE"])
    
    chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    chrome.quit
    
