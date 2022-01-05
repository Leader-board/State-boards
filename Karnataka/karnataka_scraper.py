import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import multiprocessing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def main_thread(init):
    driver = webdriver.Chrome('C:/chromedriver.exe') 
    # each process is given 10000 roll numbers to analyse
    for student_code in range(100000 + 10000*init + 1, 100000 + 10000*(init + 1) + 1):
        try:
            driver.get('http://karresults.nic.in/indexPUC_2020.asp')
            schoolcode = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form/div/input')
            schoolcode.send_keys(student_code)
            schoolcode.send_keys(Keys.ENTER)
            while(driver.current_url == 'http://karresults.nic.in/indexPUC_2020.asp'):
                time.sleep(0.1)
            # check if results even exist
            checker = driver.find_elements_by_xpath('/html/body/div[2]/div/h3')
            if (len(checker) != 0):
                continue # don't bother, no results exist
            # otherwise, should display the results now
            name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[1]/td[2]/span").text
            regno = driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[2]/td[2]/span").text
            subject1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[2]/td[1]").text
            subject1theory = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[2]/td[2]").text
            subject1practical = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[2]/td[3]").text
            subject1total = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[2]/td[4]").text
            subject2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[3]/td[1]").text
            subject2theory = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[3]/td[2]").text
            subject2practical = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[3]/td[3]").text
            subject2total = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[3]/td[4]").text
            partAtotal = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table/tbody/tr[4]/td[2]/span").text
            subject3 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[1]").text
            subject3theory = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[2]").text
            subject3practical = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[3]").text
            subject3total = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[2]/td[4]").text
            subject4 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[3]/td[1]").text
            subject4theory = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[3]/td[2]").text
            subject4practical = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[3]/td[3]").text
            subject4total = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[3]/td[4]").text
            subject5 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[4]/td[1]").text
            subject5theory = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[4]/td[2]").text
            subject5practical = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[4]/td[3]").text
            subject5total = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[4]/td[4]").text
            subject6 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[5]/td[1]").text
            subject6theory = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[5]/td[2]").text
            subject6practical = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[5]/td[3]").text
            subject6total = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[5]/td[4]").text
            partBtotal = driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[6]/td[2]/span").text
            grandtotal = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[1]/td[2]").text
            finalresult = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]").text
            f = open(str(student_code) + ".txt", "w")
            f.write(name + "|" + regno + "|" + subject1 + "|" + subject1theory + "|" + subject1practical + "|" + subject1total + "|" + subject2 + "|" + subject2theory + "|" + subject2practical + "|" + subject2total + "|" + partAtotal + "|" + subject3 + "|" + subject3theory + "|" + subject3practical + "|" + subject3total + "|" +subject4 + "|" + subject4theory + "|" + subject4practical + "|" + subject4total + "|" +subject5 + "|" + subject5theory + "|" + subject5practical + "|" + subject5total + "|" +subject6 + "|" + subject6theory + "|" + subject6practical + "|" + subject6total + "|" + partBtotal + "|" + grandtotal + "|" + finalresult + "\n")
            f.close()
        except Exception as e:
            print("Error occurred because " + str(e))
    driver.quit()
if __name__ == '__main__':
    NUMBER_OF_THREADS = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=NUMBER_OF_THREADS)
    # now use a pool. To minimise the number of windows being opened, we schedule them in batches
    pool.map(main_thread, range(0, 90))