from selenium import webdriver
from time import sleep
from secrets import password

# making sure that the webdriver is successfully accessible via bin

# adding a class to have methods that take on a variety of tasks.
class InstaBot: 
    def __init__(self, username, password) : # init function will be run when we create a new version of the class InstaBot
        self.driver = webdriver.Chrome(r"/usr/local/bin/chromedriver") # starting up the webdriver
        self.driver.get("https://instagram.com")
        sleep(2) # here we wait for the intial page to load and keep it on the screen
        self.username = username #saving a reference to our username incase we need it in other methods
        # here we are using x path to find a particular element on instagram's page, the login button
        # by clicking on an element, and right clikcing and pressing copy, then pressing "full x path"
        # we can grab an element by it's x path using .find_element_by_xpath()
        # self.driver.find_element_by_xpath(' /html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]')        
        
        # An alternative to the full xpath, searching for a link that contains the text "log in"
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        #     .click()      

        # finding input where name = "username" 
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        
        # submiting username and password info
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(6)
        # pressing button "not now" to not save info at this time
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        # pressing button "not now" to not turn on notifications at this time
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)




my_bot = InstaBot("brunoreyes01", password) # saving the bot in a variable
# now we are calling the file, making sure the function works: python3 main.py