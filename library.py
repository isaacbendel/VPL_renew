PATH_TO_CHROMEDRIVER = '/home/user/Downloads/chromedriver'
LOGIN_INFO = [('LIBRARYCARD1','PIN1'),('LIBRARYCARD2','PIN2')]
PATH_FOR_SCREENSHOTS = '/home/user/Pictures'
TIME_FACTOR = 1

from selenium import webdriver
import time
import datetime
import os


def login(browser):
    time.sleep(1)
    username_box = browser.find_element_by_xpath('//input[@name="name"]')
    username_box.clear()
    username_box.send_keys(login_info[0])
    password_box = browser.find_element_by_xpath('//input[@name="user_pin"]')
    password_box.clear()
    password_box.send_keys(login_info[1])
    login_button = browser.find_element_by_xpath('//input[@name="commit"]')
    time.sleep(0.5)
    login_button.click()
    time.sleep(1)

def renew(browser):
    browser.get('https://vaughanpl.bibliocommons.com/checkedout/index/out')
    time.sleep(4)
    select_all_button = browser.find_element_by_xpath('//span[@class="check"]')
    select_all_button.click()
    time.sleep(1)
    renew_button = browser.find_element_by_xpath('//a[@data-action="/checkedout/renew_confirmation"]')
    renew_button.click()
    time.sleep(5)
    filename_for_screenshot = os.path.join(PATH_FOR_SCREENSHOTS,'Renewal_for_account_' + str(login_info[0]) + '_on_' + datetime.datetime.today().strftime('%D').replace('/','-') + '.png')
    browser.get_screenshot_as_file()
    browser.get('https://vaughanpl.bibliocommons.com/user/logout')
    browser.sleep(3)


def main():
    browser = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
    browser.get('https://vaughanpl.bibliocommons.com/user/login')
    
    try:
        for login_info in LOGIN_INFO:
            login(browser, login_info)
            renew(browser, login_info)
    except:
        print('An error occured. Probably due to slow response from website. Try increasing value "TIME_FACTOR" variable.') 
    
    browser.close()
    

if __name__ == "__main__":
    main()


