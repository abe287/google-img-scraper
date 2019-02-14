from selenium import webdriver
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time

path = os.path.dirname(__file__)
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
link_list = []


print("What images would you like to download?")
keyword = input()

print("How many images?")
limit = int(input())


x = (limit / 50) - 5
int(x)
print("Starting...")
chromedriver = "chromedriver"
#/Users/abe287/Desktop/WebAutomation/chromedriver
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)
driver.get("http:google.com/images")

searchbar = driver.find_element_by_name('q')
searchbar.clear()
searchbar.send_keys(keyword)


button = driver.find_element_by_class_name('Tg7LZd')
button.click()



# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page 
    time.sleep(1)


    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height




j=0
while j < x:
    time.sleep(1)
    try:
        load = driver.find_element_by_id('smb');
        load.click()
    except NoSuchElementException as exception:
        print ("Element not found and test failed")

    j+=1

print("Grabbing Links...")
elems = driver.find_elements_by_xpath('//*[@src]')
for elem in elems:
    link_list.append(elem.get_attribute("src"))

del link_list[0:3]
link_list.pop()
link_list.pop()
link_list.pop()
link_list.pop()
link_list.pop()
link_list.pop()
link_list.pop()
link_list.pop()

print("Downloading Images to Folder...")
i = 0
while i<limit:
	print("Downloading Image"+str(i))
	urllib.request.urlretrieve(link_list[i], str(path)+keyword+str(i)+".jpg")
	#(link to download, name of location+filename)
	i += 1
#/Users/abe287/Desktop/WebAutomation/
print("done...")
driver.close()






