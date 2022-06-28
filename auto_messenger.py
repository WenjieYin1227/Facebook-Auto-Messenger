from selenium import webdriver
import time,os,uuid,json,re,sched, timeit
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import random,time,getpass,csv





chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('log-level=3')
uindex=0


def BOT_THREAD_STARTER(driver,EMAILID,PASSWORD,your_id,minimum_contacts,max_wait_for_reply,message):
    global uindex
     
    try:
        print("Loading facebook.com ...")

        driver.get('https://web.facebook.com/')
        time.sleep(5)
        print("Starting Logging in Procees ...")

        driver.find_element_by_id('email').send_keys(EMAILID)
        driver.find_element_by_id('pass').send_keys(PASSWORD)
        time.sleep(3)
        driver.find_element_by_name('login').click()
        print("Logging in ...")
        time.sleep(15)

        from marketplace_contact_fetch import ContactFetcher

        # if os.path.exists(os.path.join(os.getcwd(),'fresh_fetched_contacts.txt')):pass
        # else: ContactFetcher(driver,int(your_id),int(minimum_contacts))
        ContactFetcher(driver,int(your_id),int(minimum_contacts))



        IDLIST = [] 
        with open('fresh_fetched_contacts.txt', 'r') as file:
            for line in file.readlines():
                IDLIST.append(str(line).strip())
                    
        MESSAGES_LOG=[ {"id":x,"sessional_len":0,"init_messgae_handler":0} for x in IDLIST]



        BOTINITTIME = int(time.time())
        total_received_messages = 0
        loop_counter=0





        while True:

            for index,TARGETCHATID in enumerate(IDLIST[:int(minimum_contacts)]):
                SESSIONAL_LEN = 0
                print("Opening Messenger ...")
                driver.get('https://web.facebook.com/messages/t/{}'.format(TARGETCHATID))
                print("Messenger Loaded ... ")
                time.sleep(20)

                def CHAT_CONTEXT_HANDLER(): 
                    try:
                        time_locker = time.time()

                        while True:   
                            print("** Refreshing Chat Inbox")
                            time.sleep(3)

                            time.sleep(2)
                            print("Sending hello message")
                            textAreaElem = driver.find_element_by_xpath(
                                "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div")
                            try:
                                for char in str(message):
                                    textAreaElem.send_keys(str(char))
                                    time.sleep(0.05)
                                time.sleep(2)
                                time.sleep(2)
                                sender = driver.find_element_by_xpath(
                                    '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div')
                                sender.click()
                            except:
                                print("stale element reference")
                                continue

                            print("#"*20)
                            break
                    except Exception as e:
                        print(e)
                        print(e.__traceback__.tb_lineno)

                CHAT_CONTEXT_HANDLER()
        return True
    except Exception as e:
        print(e)
        return False            


