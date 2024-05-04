import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SNOS ACCOUNTA \n for you!")
colored_banner = colored(ascii_banner, color='red') 

print(colored_banner)
device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()
print(colored(f"Софт от: https://t.me/BelugaFan0", 'yellow'))
print(colored(f"Устройство: {device_name}", 'red'))
print(colored(f"Время запуска софта: {current_time}", 'cyan'))
print(colored(f"IP-адрес (если стоит ваш, проверьте ваш прокси): {ip_address}", 'yellow'))
print(colored(f"Для установки прокси, нужен сам прокси с портом SOCKS5, потом зайдите в Настройки устройства и найдите прокси.", 'blue'))

def check_data_files():
    try:
        with open('text.txt', 'r') as text_file:
            text = text_file.read().splitlines()
        with open('num.txt', 'r') as num_file:
            numbers = num_file.read().splitlines()

        if not text or not numbers:
            print("НЕТ ДАННЫХ, проверьте указанные вами данные.")
            return False
        return True

    except FileNotFoundError:
        print("Ошибка: файлы были удалены / владелец репозиторий удалил нужные файлы.")
        return False


if not check_data_files():
    exit()

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }

    try:
        response = requests.post(url, data=payload, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"\33[92mОтправлено жалоба\n Кол-во (лимит 100000)", yukino, "УЖЕ ОТПРАВЛЕНО\33[0m")
        else:
            print(colored(f"Ошибка отправки, возможно проблема в прокси, либо не правильно указан num.txt:", 'red'))
    except requests.exceptions.RequestException as e:
        print(colored(f"Ошибка, проверьте свой интернет либо прокси: {e}", 'red'))

with open('num.txt', 'r') as num_file:
    contact = num_file.read().splitlines()

with open('text.txt', 'r') as text_file:
    text = text_file.read().splitlines()

limit = 100000

while yukino < limit:
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    print(f"Отправка жалобы №{yukino}...")
    send_complaint(chosen_text, chosen_contact)
    time.sleep(1) 
