import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://internshala.com")


def login(username, password):
    login_navbar = driver.find_element(By.XPATH, "//*[@id='header']/div/nav/div[3]/ul/li[4]/button")
    login_navbar.click()

    username_field = driver.find_element(By.XPATH, '//*[@id="modal_email"]')
    password_field = driver.find_element(By.XPATH, '//*[@id="modal_password"]')

    username_field.send_keys(username)
    password_field.send_keys(password)

    submit = driver.find_element(By.XPATH, '//*[@id="modal_login_submit"]')
    submit.click()

    time.sleep(10)


def navigate_to_edit_resume():
    hover = ActionChains(driver)
    edit_resume_navbar = driver.find_element(By.XPATH, '//*[@id="header"]/div/nav/div[3]/ul/li[6]/a')
    hover.move_to_element(edit_resume_navbar).perform()

    edit_resume = driver.find_element(By.XPATH, '//*[@id="profile-dropdown"]/div/div/div/ul/div/li[2]/a')
    hover.move_to_element(edit_resume).click().perform()


def add_position(position_name):
    get_add_button = driver.find_element(By.XPATH, '//*[@id="por-resume"]')
    get_add_button.click()
    time.sleep(5)

    get_textarea = driver.find_element(By.XPATH, '//*[@id="other_experiences_por_description"]')
    get_textarea.send_keys(position_name)
    time.sleep(5)

    save = driver.find_element(By.XPATH, '//*[@id="por-submit"]')
    save.click()
    time.sleep(5)

