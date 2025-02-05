from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def main():
    testCorrectLoginInfo()
    testWrongLoginInfo()
    testLogOut()
    addToCart()
    removeItemFromCartItself()

def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    service = Service(executable_path="chromedriver.exe", chrome_options=chrome_options)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def testCorrectLoginInfo():
    driver = setup()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()
    logout_btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span")
    assert logout_btn.is_displayed()
    driver.quit()

def testWrongLoginInfo():
    driver = setup()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauc")
    login = driver.find_element(By.ID, "login-button")
    login.click()
    errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
    assert errorMessage.is_displayed()
    driver.quit()

def testLogOut():
    driver = setup()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    login = driver.find_element(By.ID, "login-button")
    assert login.is_displayed()
    driver.quit()

def addToCart():
    driver = setup()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()
    addItem = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    addItem.click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    cartItemPresent = driver.find_element(By.CLASS_NAME, "cart_item")
    assert cartItemPresent.is_displayed()
    driver.quit()

def removeItemFromCartItself():
    driver = setup()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login = driver.find_element(By.ID, "login-button")
    login.click()
    addItem = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
    addItem.click()
    cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    removeButton = driver.find_element(By.NAME, "remove-sauce-labs-bike-light")
    removeButton.click()
    try:
        # ako nije prikazan onda znaci da je test prosao
        # no zbog toga sto ce is_displayed() vratiti error moramo ga postaviti u try: blok
        assert removeButton.is_displayed()
    except:
        driver.quit()

if __name__=="__main__":
    main()