import time
import psutil
import os

last_recevied = psutil.net_io_counters().bytes_recv
last_send = psutil.net_io_counters().bytes_sent
last_total = last_recevied+last_send

clear = lambda: os.system('cls')
clear()

while True:
    bytes_recevied = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_recevied + bytes_sent

    new_recevied = bytes_recevied - last_recevied
    new_sent = bytes_sent - last_send
    new_total = bytes_total - last_total

    mb_new_recevied = new_recevied / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024

    print(f'\r{mb_new_recevied:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total',end='\r')

    last_recevied = bytes_recevied
    last_send = bytes_sent
    last_total = bytes_total

    time.sleep(1)