from selenium import webdriver
from selenium.webdriver.common.by import By
from config import username as user_name, password as pass_word, repository_name,url
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class MyClass:
    
    def __init__(self):
        self.logger = logging.getLogger('withselenium')
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('logfile.log',mode='a')
        formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        logging.info('initialised chrome')

    def login(self):
        self.logger.info('login started')
        self.driver.get(f'{url}/login')

        username = self.driver.find_element(by=By.ID, value='login_field')
        username.send_keys(user_name)

        password = self.driver.find_element(by=By.ID, value="password")
        password.send_keys(pass_word)

        signin = self.driver.find_element(
            by=By.CLASS_NAME, value="js-sign-in-button")
        signin.click()
        self.logger.info('login terminated')

    def create_repo(self):
        self.logger.info('creating repository started')
        new_repo = WebDriverWait(self.driver, 2000).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div/aside/div[2]/div[1]/div/h2/a")))
        new_repo.click()

        repositoryname = self.driver.find_element(
            by=By.XPATH, value='//*[@id="repository_name"]')
        repositoryname.send_keys(repository_name)

        create_repo = WebDriverWait(self.driver, 2000).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='new_repository']/div[4]/button")))
        create_repo.click()
        self.logger.info('Repo created successfully')

    def del_repo(self):
        self.logger.info('deleting repository')

        goto_settings = WebDriverWait(self.driver, 2000).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div/main/div[1]/nav/ul/li[9]/a")))
        goto_settings.click()

        delete_rep = WebDriverWait(self.driver, 2000).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div/main/div[2]/div/div/div[2]/div/div/div/div[10]/ul/li[4]/details/summary")))
        delete_rep.click()

        del_confirm_msg = self.driver.find_element(by = By.XPATH,value=
            '/html/body/div[6]/div/main/div[2]/div/div/div[2]/div/div/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input')
        del_confirm_msg.send_keys(f"{user_name}/{repository_name}")

        del_confirm = WebDriverWait(self.driver, 2000).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[6]/div/main/div[2]/div/div/div[2]/div/div/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button/span[1]")))
        del_confirm.click()
        self.logger.info(f'Deleted repository({repository_name}) successfully')

    def get_repos(self):
        self.logger.info('Initiating Getting list of repos')
        get_rep = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/header/div[7]/details/summary")))
        get_rep.click()

        get_rep2 = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/header/div[7]/details/details-menu/a[2]")))
        get_rep2.click()
        
        items = self.driver.find_element(by=By.ID,value=
            "user-repositories-list").find_elements(by=By.TAG_NAME,value="li")
        for item in items:
            print(item.text)
            print("---------")
        self.logger.info('Repo list retrieved ')

    def __del__(self):
        self.driver.close()
        self.logger.info('chrome window closed ')
