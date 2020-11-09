from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Chrome()

@given('I visit instagram')
def visit(context):
    driver.get('https://www.instagram.com/')

@when('I see log in form')
def check(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.NAME, "username")))

@then('login with username "{username}" and password "{password}"')
def login(context, username, password):
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)

@then('I close popup "Accept"')
def look(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]'))).click()

@then('I close popup "Şimdi Degil"')
def close(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//button[text()="Şimdi Değil"]'))).click()

@when('I click here "message button"')
def push(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.CLASS_NAME, "xWeGp"))).click()

@then('I click here "third message"')
def message(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[3]/a'))).click()

@then('I click here "send message"')
def send(context):
    wait = WebDriverWait(driver, 10)
    wait.until(presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))).send_keys('MESSAGE_TEXT' + Keys.ENTER)

