import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import multiprocessing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
codelimit = [181,143,107,128,139,82,216,218,163,191,261,61,171,108,12,9,6]
def main_thread(school_code):
    driver = webdriver.Chrome('C:/chromedriver.exe') 
    driver.get('http://keralaresults.nic.in/dhse20bck932/swr_dhse.htm')
    schoolcode = driver.find_element_by_name('treg')
    schoolcode.send_keys(school_code)
    schoolcode.send_keys(Keys.ENTER)
    # should display the results now
    time.sleep(5) # will take that much time to load, be conservative
    # WebDriverWait(driver, 10).until(EC.staleness_of(schoolcode))
    results_table = driver.find_elements_by_xpath("/html/body/form/table/tbody/tr/td/span/div/center/table/tbody/tr") 
    f = open(school_code + ".txt", "w")
    for res in results_table:
        # print(res.text)
        f.write(res.text + "\n")
    f.close()
    driver.quit();

def schcodegenerator(distcode, schdist):
    schcode = ""
    if (distcode + 1 <= 9):
        schcode = schcode + "0"
    schcode = schcode + str((distcode + 1))
    if (schdist < 100):
        schcode = schcode + "0"
    if (schdist < 10):
        schcode = schcode + "0"
    schcode = schcode + str(schdist)
    return schcode # a string
# driver code
schlist = [] # list of all school codes
if __name__ == '__main__':
    distcode = 0
    schdist = 1
    NUMBER_OF_THREADS = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=NUMBER_OF_THREADS)
    while (distcode < len(codelimit)):
        if (schdist <= codelimit[distcode]):
            # generate school code string
            sch_code = schcodegenerator(distcode, schdist)
            schlist.append(sch_code)
            schdist = schdist + 1
        else:
            schdist = 1
            distcode = distcode + 1
    # now use a pool
    pool.map(main_thread, schlist) # run a pool with a suitable number of processes