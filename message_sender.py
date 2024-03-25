import csv
import pyautogui as pgui
from time import sleep
import re
from info import *

def clean_phone_number(number):
                cleaned_number = re.sub(r'[\s()-]', '', number)
                return cleaned_number

def read_csv_file(file_path):
    #data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Example usage
            number = clean_phone_number(row[4])
            name = row[0]
            
            
            if "Phone" not in number:
               print(name, number)
               send_message(name, number)
               sleep(1)
               
def send_message(name, number):
    pgui.click(1328,60)
    sleep(1)
    pgui.typewrite(f"{number}")
    pgui.press('enter')
    sleep(1)
    pgui.typewrite(f"Hello {name}, my name is {yourname} from AKL. We're having {event_and_time}, hope to see you here", interval=0.1)
    sleep(1)
    pgui.press('enter')
    sleep(2)
    pgui.click(x=782, y=68)
    sleep(1)

def test_code():
    send_message("test", test_phone_number)
    send_message("test2", test_phone_number)
    send_message("test3", test_phone_number)
    send_message("test4", test_phone_number)

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            sleep(1)
    print("Test code ran successfully")
        
file_path = csv_name

#test_code()
#read_csv_file(file_path)
