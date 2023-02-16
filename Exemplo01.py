from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

login_url = 'https://sig.ifsc.edu.br/sigaa/public/home.jsf'

driver.get(login_url)
driver.implicitly_wait(10)

print("Clica no link de acesso ao login")

try:
    driver.find_element(By.XPATH,'//*[@id="acesso"]/ul/li[2]/a').click()
except:
    driver.quit()
    print('Erro ao localizar link de acesso á tela de login')


print('Envia os dados para o login')
username = ''
password = ''

try:
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[1]/td/input').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/table/tbody/tr[2]/td/input').send_keys(username,Keys.ENTER)
except:
    driver.quit()
    print('Erro ao enviar dados para o login')

print("Clica em sair")

sleep(5)

try:
    driver.find_element(By.XPATH, '//*[@id="info-sistema"]/div/span[3]/a').click()
except:
    driver.quit()
    print("Erro ao tentar sair")

print('Teste realizado com sucesso')
driver.quit()