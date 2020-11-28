from selenium import webdriver
from time import sleep
import sys
sys.path.insert(1,'/Users/brunoreyes/Desktop/Code/Python/')
from insta_bot_secrets import password

# making sure that the webdriver is successfully accessible via bin

# Created a class to contain methods that take on a variety of tasks.
class InstaBot: 
    def __init__(self, username, password) : # init function will be run when we create a new version of the class InstaBot
        self.driver = webdriver.Chrome(r"/usr/local/bin/chromedriver") # starting up the webdriver
        self.driver.get("https://instagram.com")

        sleep(2) # sleep is used to simulate a delay in the program, giving the method or function time to complete it's task, 
        # in this case, execution is suspended for 2 seconds.
        #  
        self.username = username #saving a reference to our username incase we need it in other methods
        # here we are using x path to find a particular element on instagram's page, the login button
        # by clicking on an element, and right clikcing and pressing copy, then pressing "full x path"
        # we can grab an element by it's x path using .find_element_by_xpath()

        # full xpath:
        # self.driver.find_element_by_xpath(' /html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]')        
        
        # An alternative to the full xpath, searching for a link that contains the text "log in"
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\     

        # finding input where name = "username" 
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(password)
        
        # submiting username and password info
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)

        # pressing button "not now" to not save info at this time
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

        # pressing button "not now" to not turn on notifications at this time
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    
    def get_unfollowers(self):
        # heading to my profile page to access followers and following lists
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()   
        sleep(2)

        # pressing my profile pic icon, and heading into the profile sub menu
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Profile')]")\
        #     .click()   
        # sleep(2)

        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()  

        # pacing the list of followers into a variable
        following = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
                .click()  

        followers = self._get_names()

        # list comprehension to find users that are within the 'following' list that aren't in 'followers' list,
        # and placing them into the variable: not_following_back
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self): #making a method private using "_" in front
        sleep(1)

        # This piece is solely used if the suggestion button pops up at the end of each scroll list
        # sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        # javascript code is what's in the execute_script
        # self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
     

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")


        # here each scroll considers the height of the box from the height of the box we are going 
        # to scroll. This goes on until the ht is the same as the last_ht we tried to scroll
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        
        
        links = scroll_box.find_elements_by_tag_name('a')

        # here is a list comprehension that gets the text from each 'a' tag if name != ''
        names = [name.text for name in links if name.text != '']
        # print(names)

        #  exiting out of the following box via clicking the exit button
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]")\
            .click()
        return names


my_bot = InstaBot("brunoreyes01", password) # saving the bot in a variable
# calling the file, making sure the function works: python3 main.py

# I'm running the get followers method via interactive window: python3 -i main.py
my_bot.get_unfollowers()
