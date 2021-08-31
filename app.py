import os
import time
import subprocess
import requests
import progressbar
import urllib3 
import pathlib
from tqdm import tqdm
import math

def checkAdbShell():
    if (os.system('adb shell reboot poweroff')!= 0):
        print('NO ADB DEVICE')
        print('PLEASE, BOOT INTO TWRP, HOLD VOLUME UP + POWER BUTTON')
        return False
    else:
        return True

def downloadRom():

    print("--- DOWNLOADING MIUI 12.5-STABLE ---")

    url = f"https://downloads.sourceforge.net/project/xiaomi-eu-multilang-miui-roms/xiaomi.eu/MIUI-STABLE-RELEASES/MIUIv12/xiaomi.eu_multi_HM7_V12.5.1.0.QFLCNXM_v12-10.zip?ts=gAAAAABhLi4_PDax5KWgPnddyi5DSocH-MgX-55neKxY4hjGSTzgaaKFZw8Et3-t0t-W_spIx4vNU4ECfRvjRGC4zCdZYUGTEg%3D%3D&r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fxiaomi-eu-multilang-miui-roms%2Ffiles%2Fxiaomi.eu%2FMIUI-STABLE-RELEASES%2FMIUIv12%2Fxiaomi.eu_multi_HM7_V12.5.1.0.QFLCNXM_v12-10.zip%2Fdownload%3Fuse_mirror%3Djztkft%26r%3Dhttps%253A%252F%252Fsourceforge.net%252Fprojects%252Fxiaomi-eu-multilang-miui-roms%252Ffiles%252Fxiaomi.eu%252FMIUI-STABLE-RELEASES%252FMIUIv12%252Fxiaomi.eu_multi_HM7_V12.5.1.0.QFLCNXM_v12-10.zip%252Fdownload%253Fuse_mirror%253Dkumisystems%2526use_mirror%253Dkumisystems%2526r%253Dhttps%25253A%25252F%25252Fsourceforge.net%25252Fprojects%25252Fxiaomi-eu-multilang-miui-roms%25252Ffiles%25252Fxiaomi.eu%25252FMIUI-STABLE-RELEASES%25252FMIUIv12%25252F"
    # Streaming, so we can iterate over the response.
    r = requests.get(url, stream=True)

    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0 
    with open('xiaomi.eu_multi_HM7_V12.5.1.0.QFLCNXM_v12-10.zip', 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
            wrote = wrote  + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong") 

def downloadMagisk():
    print("--- DOWNLOADING MAGISK ---")

    url = f"https://magiskmanager.com/go/download"
    # Streaming, so we can iterate over the response.
    r = requests.get(url, stream=True)

    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0)); 
    block_size = 1024
    wrote = 0 
    with open('Magisk-v23.0.zip', 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
            wrote = wrote  + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong") 


print(' _____  _____  _____  ________      _______ ')
print('|  __ \|  __ \|  __ \|  ____\ \    / / ____|')
print('| |  | | |__) | |  | | |__   \ \  / /| |__  ')
print('| |  | |  ___/| |  | |  __|   \ \/ / |___ \ ') 
print('| |__| | |    | |__| | |____   \  /   ___) |')
print('|_____/|_|    |_____/|______|   \/   |____/ ') 
print('\n')

print('-----------------------------------------------------------------')
print('     DISCLAMER')
print('\n')

print('I am not responsible for bricked devices, dead SD cards \n thermonuclear war, or the current economic crisis caused by you following \n these directions. YOU are choosing to make these modificiations, and if \n you point your finger at me for messing up your device, I will LMAO at you.')                                      
print('-----------------------------------------------------------------')


os.system("Pause")
print(os.system('fastboot devices'))
print('--- Flashing Original Recovery ---')
os.system('fastboot flash recovery img' + os.sep + 'recovery.img')
print('--- Flashing LRTeam Recovery ---')
os.system('fastboot flash recovery img' + os.sep + 'twrplrteam.img')
print('PLEASE, BOOT INTO TWRP, HOLD VOLUME UP + POWER BUTTON')

while (checkAdbShell() == False):
    time.sleep(3)


print('--- FORMATTING DATA, TYPE YES IF REQUIRED ---')
#os.system('adb shell twrp format data')
print('CLEANING PARTITIONS')
os.system("Pause")
os.system('adb shell twrp wipe cache')
os.system('adb shell twrp wipe dalvik')
os.system('adb shell twrp wipe data')
os.system('adb shell twrp wipe cache')

downloadRom()
downloadMagisk()

print('------------------------------------------------------------------')
print('------------------------------------------------------------------')
print('NOW COPY DOWLOADED FILES TO PHONE INTERNAL MEMORY, THEN PRESS ENTER')
print('------------------------------------------------------------------')
print('------------------------------------------------------------------')


os.system("Pause")

print('flashing ROM')
os.system('adb shell twrp install xiaomi.eu_multi_HM7_V12.5.1.0.QFLCNXM_v12-10.zip')
print('flashing Magisk')
os.system('adb shell twrp install Magisk-v23.0.zip')
os.system('adb shell twrp reboot')




    

