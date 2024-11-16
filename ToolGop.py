import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37mVMT\033[1;31m] \033[1;37m➩  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def banner():
 banner = f"""
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;94m══\x1b[1;96m══
\033[1;33m__     __       __  __             _       _____ _            
\033[1;35m\ \   / /   _  |  \/  | __ _ _ __ | |__   |_   _(_) ___ _ __  
\033[1;36m \ \ / / | | | | |\/| |/ _` | '_ \| '_ \    | | | |/ _ \ '_ \ 
\033[1;31m  \ V /| |_| | | |  | | (_| | | | | | | |   | | | |  __/ | | |
\033[1;32m   \_/  \__,_| |_|  |_|\__,_|_| |_|_| |_|   |_| |_|\___|_| |_|
\033[1;31m────────────────────────────────────────────────────────────── 
\033[1;31m[\033[1;32m●\033[1;31m]  ADMIN: \033[1;36mVũ Mạnh Tiến     \033[1;36mFB: \033[1;31m𝑽𝒖\033[1;32m𝑴𝒂𝒏𝒉\033[1;35m𝑻𝒊𝒆𝒏
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;94m══\x1b[1;96m══
\033[1;31m[\033[1;32m●\033[1;31m]      \033[1;32m╔══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\033[1;31m══\x1b[1;94m══\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m═══╗
\033[1;31m[\033[1;32m●\033[1;31m]      \033[1;32m║  \033[1;33m🌺      🔰     \033[1;33mTOOL GỘP ALL      🔰     🌺 \033[1;32m ║
\033[1;31m[\033[1;32m●\033[1;31m]      \033[1;32m╚══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\033[1;31m══\x1b[1;94m══\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m═══╝
\033[1;31m[\033[1;32m●\033[1;31m] \033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\x1b[1;94m══\x1b[1;96m══
\033[1;31m──────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush()
  sleep(0.00125)
import requests
from time import strftime
ngay=int(strftime('%d'))

print('\033[1;34m🌺 Chạy Tiến Trình 🌺')
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print('')

print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m1\033[1;31m] \033[1;32mTool Reg Page Pro5 \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m2\033[1;31m] \033[1;32mTool Reg Page Pro5 + Úp Avt \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m3\033[1;31m] \033[1;32mTool Share Ảo Pro5 \033[1;36m(Termux)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m4\033[1;31m] \033[1;32mTool TDS-FB Pro5 \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m5\033[1;31m] \033[1;32mTool TDS-FB \033[1;36m(Termux + PC)")

print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\033[1;32m══\x1b[1;91m══\x1b[1;94m══\x1b[1;96m══")

print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m6\033[1;31m] \033[1;32mTool Golike Auto Linkedin \033[1;36m(Termux)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m7\033[1;31m] \033[1;32mTool Golike Auto Instagram \033[1;36m(Termux)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m8\033[1;31m] \033[1;32mTool Golike Auto Threads \033[1;36m(Termux)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m9\033[1;31m] \033[1;32mTool Golike Auto TikTokv1 \033[1;36m(Termux)")

print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\033[1;32m══\x1b[1;91m══\x1b[1;94m══\x1b[1;96m══")

print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m10\033[1;31m] \033[1;32mTool Buff Follow TikTok \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m11\033[1;31m] \033[1;32mTool Zefoy Buff View TikTok \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m12\033[1;31m] \033[1;32mTool Spam SMS V1 \033[1;36m(Termux + PC)")
print("\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;31m[\033[1;36m13\033[1;31m] \033[1;32mTool Spam SMS V2 \033[1;36m(Termux)")

print("\033[1;32m╔════════════════════════════════════════════════════════════╗")
print("\033[1;32m║\033[1;34m🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎🌺🌵🌎\033[1;32m║")
print("\033[1;32m╚════════════════════════════════════════════════════════════╝")

chon = int(input('\033[1;31m[\033[1;32m●\033[1;31m] \033[1;33mNhập Số \033[1;37m: \033[1;33m'))
print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══\033[1;32m══\x1b[1;91m══")
if chon == 1 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/RegPage.py').text)
elif chon == 2 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/RegPageAvt.py').text)
elif chon == 3 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/ShareAoPro5.py').text)
elif chon == 4 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/TdsFbPro5.py').text)
elif chon == 5 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/TdsFb.py').text)
elif chon == 6 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/GolikeAutoLinkedin.py').text)
elif chon == 7 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/GolikeAutoInstagram.py').text)
elif chon == 8 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/GolikeAutoTheads.py').text)
elif chon == 9 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/GolikeAutoTikTokv1.py').text)
elif chon == 10 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/FlTiktok.py').text)
elif chon == 11 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/ToolZefoy.py').text)
elif chon == 12 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/SpamSMSv1.py').text)
elif chon == 13 :
        exec(requests.get('https://raw.githubusercontent.com/tienhoclaptrinh2005/Src_Tool/main/SpamSMSv2.py').text)

else :
        print (" Sai Lựa Chọn ")
        exit()



