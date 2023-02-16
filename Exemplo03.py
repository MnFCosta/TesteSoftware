from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup as BS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1980,1020")
options.add_argument("--log-level=3")
# options.add_argument("--headless")


driver = webdriver.Chrome(options=options)
login_url = 'https://pmc.sc.gov.br/'

driver.get(login_url)
driver.implicitly_wait(10)

print('Acessar o menu de ex-prefeitos')

try:
    #Simular o mouse passando no menu Municipios
    action = AC(driver)
    menu = driver.find_element(By.ID, "menu-item-2558")
    action.move_to_element(menu).perform()
    #Simular o click do menu ex-prefeitos
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'menu-item-93281'))).click()

except:
    driver.quit()
    print("Deu bigode piazão")

print("Copiar os dado da tabela de ex-prefeitos")

try:
    elemento = driver.file_element(By.XPATH, '//*[@id="post-19376"]/div[1]')
    conteudo_html = elemento.get_attribute("outerHTML")
    soup = BS(conteudo_html,'html.parser')
    tabela = soup.find(name='table')
    with open('lista.csv', "w") as arquivo:
        for row in soup.find_all('tr'):
            line=''
            for col in row.find_all('td'):
                line = line + col.text + ';'
            arquivo.write(line+'\n')
    arquivo.close()
except:
    driver.quit()
    print('deu ruim')

print("Deu bom pia")
driver.quit()