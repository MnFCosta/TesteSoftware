from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

login_url = 'https://moodle.ifsc.edu.br/'

driver.get(login_url)
driver.implicitly_wait(10)

print("Clica no link de acesso ao login")

print('Envia os dados para o login')
username = ''
password = ''

try:
    driver.find_element(By.XPATH, '//*[@id="inputName"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys(password,Keys.ENTER)
except:
    driver.quit()
    print('Erro ao enviar dados para o login')

print("Clica em sair")

sleep(5)

try:
    driver.find_element(By.XPATH, '//*[@id="yui_3_17_2_1_1676504442766_258"]').click()
    driver.find_element(By.XPATH, '//*[@id="action-menu-0-menu"]/li[8]/a').click()

except:
    driver.quit()
    print("Erro ao tentar sair")

print('Teste realizado com sucesso')
driver.quit()