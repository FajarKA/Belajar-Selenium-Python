import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TestLogin(unittest.TestCase): 

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys("alhamalfjr@gmail.com") 
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("asd123asd") 
        time.sleep(2)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_welcome = driver.find_element(By.ID,"swal2-title").text 
        response_berhasil_login = driver.find_element(By.ID,"swal2-content").text 
        
        self.assertEqual(response_welcome, "Welcome fajar")
        self.assertEqual(response_berhasil_login, "Anda Berhasil Login")
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(2)

    def test_login_with_empty_email_and_password(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys("")
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(2)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_user_not_found = driver.find_element(By.ID,"swal2-title").text
        response_gagal_login = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_user_not_found, "User's not found")
        self.assertEqual(response_gagal_login,"Email atau Password Anda Salah")
        driver.find_element(By.XPATH,"//button[text()='OK']").click()
        time.sleep(2)

    def test_login_with_email_not_register(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys("alhamalfka@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("asd123asd")
        time.sleep(2)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_user_not_found = driver.find_element(By.ID,"swal2-title").text
        response_gagal_login = driver.find_element(By.ID,"swal2-content").text
        
        self.assertEqual(response_user_not_found,"User's not found")
        self.assertEqual(response_gagal_login,"Email atau Password Anda Salah")
        driver.find_element(By.XPATH,"//button[text()='OK").click()
        time.sleep(2)

    def test_login_with_wrong_password(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys("alhamalfjr@gmail.com")
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("qwe123qwe")
        time.sleep(2)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_user_not_found = driver.find_element(By.ID,"swal2-title").text
        response_gagal_login = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_user_not_found,"User's not found")
        self.assertEqual(response_gagal_login,"Email atau Password Anda Salah")
        driver.find_element(By.XPATH,"//button[text()='OK").click()
        time.sleep(2)

    def test_login_with_an_email_and_password_that_has_been_registered_but_uses_capital_letters(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        driver.find_element(By.ID,"email").send_keys("ALHAMALFJR@GMAIL.COM") 
        time.sleep(2)
        driver.find_element(By.ID,"password").send_keys("ASD123ASD") 
        time.sleep(2)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_welcome = driver.find_element(By.ID,"swal2-title").text 
        response_berhasil_login = driver.find_element(By.ID,"swal2-content").text 
        
        self.assertEqual(response_welcome, "Welcome fajar")
        self.assertEqual(response_berhasil_login, "Anda Berhasil Login")
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
        time.sleep(2)



    

    def tearDown(self): 
        self.driver.close() 
  
# execute the script 
if __name__ == "__main__": 
    unittest.main() 