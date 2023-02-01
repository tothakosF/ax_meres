import time
from selenium import webdriver
from selenium.webdriver.common.by import By

while True:
    option = webdriver.ChromeOptions()
    option.add_argument("incognito")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(
        executable_path='C:\Apps\chromedriver_103\chromedriver.exe', options=option)

    driver.get("https://www.dszcmeres.hu/az-intezmenyi-onertekeles-kereteben-a-tanulok-elegedettseget-mero-kerdoiv-mechwart-55s/?preview=true")

    time.sleep(1)

    cookie = driver.find_element(By.ID, "cn-accept-cookie")
    cookie.click()

    one = driver.find_element(By.ID, "question1324_4")
    one.click()

    two = driver.find_element(By.ID, "question1326_4")
    two.click()

    three = driver.find_element(By.ID, "question1327_4")
    three.click()

    four = driver.find_element(By.ID, "question1328_4")
    four.click()

    five = driver.find_element(By.ID, "question1329_4")
    five.click()

    six = driver.find_element(By.ID, "question1330_4")
    six.click()

    seven = driver.find_element(By.ID, "question1331_4")
    seven.click()

    eight = driver.find_element(By.ID, "question1332_4")
    eight.click()

    nine = driver.find_element(By.ID, "question1333_4")
    nine.click()

    ten = driver.find_element(By.ID, "question1334_4")
    ten.click()

    eleven = driver.find_element(By.ID, "question1335_4")
    eleven.click()

    twelve = driver.find_element(By.ID, "question1336_4")
    twelve.click()

    thirteen = driver.find_element(By.ID, "question1337_4")
    thirteen.click()

    fourteen = driver.find_element(By.ID, "question1338_4")
    fourteen.click()

    fifteen = driver.find_element(By.ID, "question1339_4")
    fifteen.click()

    sixteen = driver.find_element(By.ID, "question1340_4")
    sixteen.click()

    seventeen = driver.find_element(By.ID, "question1341_4")
    seventeen.click()

    eighteen = driver.find_element(By.ID, "question1342_4")
    eighteen.click()

    nineteen = driver.find_element(By.ID, "question1343_4")
    nineteen.click()

    submitbutton = driver.find_element(
        By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div[1]/main/article/div/div[1]/form/div[3]/input[1]')

    submitbutton.click()

    time.sleep(4)

    driver.close()
