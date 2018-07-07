import time;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys


def scrape(url,message):
    driver = webdriver.Chrome("D:\Python Webscrapper\chrome\chromedriver.exe");
    driver.get(url);
    
    toggle = True;
    search = driver.find_element_by_name("stimulus")
    
    while(toggle):
        if(message == ""):
            message = input("> ")
        if(message == "exit"):
            print("closing")
            break;
        if(message == "what"):
            response = driver.find_element_by_id("line1").text
            print(response) 
            message = input("> ")
        if(message != ""):
            message = message.title() + "."

        
        time.sleep(4)
        search.send_keys(message)
        search.send_keys(Keys.RETURN)
        
        response = driver.find_element_by_id("line1").text
  
        reply = driver.find_element_by_id("line2").text
            
        if(reply == message):
            time.sleep(4)
            response = driver.find_element_by_id("line1").text
            print(response)
            if(driver.find_element_by_id("line1").text == ""):
                print("Error refreshing")
                driver.refresh()
            else:
                message = "";
            
        else:
            print("Error refreshing")
            driver.refresh()        

        
        
    
def main():
    print("Hello world!")
    message = input("> ")
    scrape("http://www.cleverbot.com/", message)
    
main()