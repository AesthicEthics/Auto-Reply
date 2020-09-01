from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from tkinter import *
import time

#Facebook

def fb():
    root = Tk()

    PATH = "C:\Program Files (x86)\chromedriver.exe"


    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("http://facebook.com")

    fbemail = ""
    fbpsw = ""

    fbemaile = driver.find_element_by_id("email")
    fbepass = driver.find_element_by_id("pass")

    fbemaile.send_keys(fbemail)
    fbepass.send_keys(fbpsw)

    fbbutton = driver.find_element_by_id("u_0_b")
    fbbutton.click()



#instagram
    #GUI Starts

def insta():
    root = Tk()
    root.title("Instagram Accelerator")
    root.configure(bg="#330000")
    Name = Label(root, text = "Recipetent Username: ", bg = "#330000")
    Name.configure(fg = "white")
    Text = Label(root, text = "Message:", bg = "#330000")
    Text.configure(fg = "white")

    Name.grid(row = 0, column = 0)
    Text.grid(row = 1, column = 0)

    getName = Entry(root, width=50, borderwidth=0)
    getName.grid(row =0, column = 1)
    getName.get()

    getMessage = Entry(root, width = 50, borderwidth =0, text = "Enter Your Message")
    getMessage.grid(row =1, column =1)
    getMessage.get()

    #Code Starts
    def code():
        email = "" #username here
        password = "" #pass here

        recv = getName.get()
        message1 = getMessage.get()

        PATH = "C:\Program Files (x86)\chromedriver.exe"

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=(PATH))

        driver.get("https://instagram.com")
        print("Headless Intialized")

        try:
            user = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME,"username"))
            )

            user.click()
            user.send_keys((email))

        except:
            driver.quit()

        try:
            passw = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            passw.click()
            passw.send_keys((password))

            button = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF")
            button.click()

            time.sleep(3)

            print("Logged In Succesfully!")
#-------
            time.sleep(5)

            button2 = driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
            button2.click()

            time.sleep(2)


            print("Notification Is Gone")
#-------

            #time.sleep(3)

            button3 = driver.find_element_by_class_name("xWeGp")
            time.sleep(2)
            button3.click()

            print("Dm's Opened")

            time.sleep(3)

            new = driver.find_element_by_class_name("wpO6b.ZQScA")
            new.click()

            print("Search Clicked")

            time.sleep(3)

            typemessage = driver.find_element_by_name("queryBox")
            typemessage.send_keys((recv))

            print("Person Selected")

            time.sleep(3)

            select = driver.find_element_by_class_name("dCJp8")
            select.click()

            print("Person Confirmed")

            time.sleep(3)

            next = driver.find_element_by_class_name("rIacr")
            next.click()

            print("Onto The Messaging")

            time.sleep(3)

#-----

            send = driver.find_element_by_class_name("focus-visible")

            print("Waiting")

            time.sleep(2)

            send.send_keys((message1))

            print("Typing Your Message!")

            time.sleep(5)

            send.send_keys(Keys.RETURN)

            print("Message Sent Succesfully!")


        except:
            driver.quit()

    #button

    button = Button(root, text = "Send", command = code, bg = "#330000")
    button.grid(row = 3, column = 1)
    button.configure(fg="white")


    root.mainloop()


#factgenerator

def fact():

    PATH = "C:\Program Files (x86)\chromedriver.exe"

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=(PATH))

    driver.get("http://randomfactgenerator.net/")
    print("Headless Intialized")

    generate = driver.find_element_by_id("b")
    generate.click()

    z = driver.find_element_by_id("z")
    texa = (z.text)
    acc = "Here's your fact: "+ texa

    print(acc)



#Intialize

root = Tk()
root.configure(bg ="#330000")
Fb = Button(root, text = "Facebook", command = fb, bg = "#330000")
Fb.configure(fg="white")
Insta = Button(root, text = "Instagram", command = insta,bg = "#330000")
Insta.configure(fg = "white")
App = Label(root, text = "Choose Your App", bg = "#330000")
App.configure(fg="white")

facts = Button(root, text = "Fact Generator!", command = fact, bg = "#330000")
facts.configure(fg="white")

App.grid(row = 0, column = 0)
Fb.grid(row = 1, column = 0)
Insta.grid(row = 2, column = 0)
facts.grid(row = 3, column = 0)

root.mainloop()
