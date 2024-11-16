import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
import requests, time
from datetime import datetime
import socket

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)

os.system("cls" if os.name == "nt" else "clear")

print('\033[0;31m •╔═════════════════════════☩══♛══☩═════════════════════════╗•')
print('\033[1;33m  ║               ██╗   ██╗███╗   ███╗████████╗             ║')
print('\033[1;95m  ║               ██║   ██║████╗ ████║╚══██╔══╝             ║')
print('\033[1;31m  ║               ██║   ██║██╔████╔██║   ██║                ║')
print('\033[1;34m  ║               ╚██╗ ██╔╝██║╚██╔╝██║   ██║                ║')
print('\033[1;95m  ║                ╚████╔╝ ██║ ╚═╝ ██║   ██║                ║')
print('\033[1;36m  ║                 ╚═══╝  ╚═╝     ╚═╝   ╚═╝                ║')
print('\033[1;36m  ║                🔰 ADMIN : VŨ MẠNH TIẾN 🔰               ║')  
print('\033[1;33m  ║         🌺      TOOL BUFF FOLLOW TIKTOK        🌺       ║')
print('\033[1;35m •╚═════════════════════════☩══✦══☩═════════════════════════╝•')
print(f" \033[0;31m ╰─> {formatted_time} |\033[0;31m IP :{ip}   ")
print(' \n ')



username=input('\033[1;33m Nhập Username Tik Tok ( Không Nhập @ ): ')
while True:
    headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6','cache-control': 'max-age=0','priority': 'u=0, i','sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'cross-site','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',}
    access=requests.get('https://tikfollowers.com/free-tiktok-followers', headers=headers)
    try:
        session=access.cookies['ci_session']
        headers.update({'cookie': f'ci_session={session}'})
        token=access.text.split("csrf_token = '")[1].split("'")[0]
        data='{"type":"follow","q":"@'+username+'","google_token":"t","token":"'+token+'"}'
        search=requests.post('https://tikfollowers.com/api/free', headers=headers, data=data).json()
        if search['success']==True:
            data_follow=search['data']
            data='{"google_token":"t","token":"'+token+'","data":"'+data_follow+'","type":"follow"}'
            send_follow=requests.post('https://tikfollowers.com/api/free/send', headers=headers, data=data).json()
            if send_follow['o']=='Success!' and send_follow['success']==True and send_follow['type']=='success':
                print('\033[1;32m 🌸 Tăng Follow Tik Tok Thành Công  ✓ ')
                continue
            elif send_follow['o']=='Oops...' and send_follow['success']==False and send_follow['type']=='info':
                try:
                    thoigian=send_follow['message'].split('You need to wait for a new transaction. : ')[1].split('.')[0]
                    phut=thoigian.split(' Minutes')[0]
                    giay=int(phut)*60
                    for i in range(giay, 0, -1):
                        print(f'\033[1;31m🍉 Vui Lòng Chờ  🍉 > {i} < Giây  ',end='\r')
                        time.sleep(0.200)
                        print(f'\033[1;32m🍉 Vui Lòng Chờ  🍉 > {i} < Giây  ',end='\r')
                        time.sleep(0.200)
                        print(f'\033[1;33m🍉 Vui Lòng Chờ  🍉 > {i} < Giây  ',end='\r')
                        time.sleep(0.200)
                        print(f'\033[1;35m🍉 Vui Lòng Chờ  🍉 > {i} < Giây  ',end='\r')
                        time.sleep(0.200)
                        print(f'\033[1;36m🍉 Vui Lòng Chờ  🍉 > {i} < Giây  ',end='\r')
                        time.sleep(0.200)
                    continue
                except:
                    print('\033[1;35m Lỗi Không Xác Định    💢    ')
                    continue
    except:
        print('\033[1;35m  Lỗi Không Xác Định    💢   ')
        continue