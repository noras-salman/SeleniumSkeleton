from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Bot:
    def __init__(self):
        self.bot= webdriver.Firefox()

    def fill_element(self,element,value):
        element.clear()
        element.send_keys(value)

    def click_element(self,element,wait):
        for i in range(10):
            try:
                element.click()
                print("not in screen")
                break
            except:
                self.scroll(100,1)
                pass

        time.sleep(wait)

    def endScroll(self,wait):
        self.bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(wait)

    def scroll(self,px,wait):
        self.bot.execute_script('window.scrollTo(0,(window.pageYOffset+'+str(px)+'))')
        time.sleep(wait)

    def navigate(self,url,wait):

        self.bot.get(url)
        time.sleep(wait)

    def exit(self):
        self.bot.quit()

    def instance(self):
        return self.bot


b=Bot()
vid_id="xxx"
# go to link 
b.navigate("https://www.youtube.com/watch?v="+vid_id,20)
# scroll down
for i in range(200):
    b.scroll(100,1)
# find a related video thumbnail 
elements=b.instance().find_elements_by_class_name("ytd-thumbnail")

# click on it 
b.click_element(elements[1],20)
# close the browser
b.exit()


#extra stuff you can do
# -------------------
#find_element_by_id
#find_element_by_name
#find_element_by_xpath
#find_element_by_link_text
#find_element_by_partial_link_text
#find_element_by_tag_name
#find_element_by_class_name
#find_element_by_css_selector

#find_elements_by_name
#find_elements_by_xpath
#find_elements_by_link_text
#find_elements_by_partial_link_text
#find_elements_by_tag_name
#find_elements_by_class_name
#find_elements_by_css_selector