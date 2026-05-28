#!/usr/bin/python3

import requests
import os

os.system("clear")

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

print(RED + r"""

_______________     ______  ___                                     
____  _/__  __ \    ___   |/  /____________________________________ 
 __  / __  /_/ /    __  /|_/ /_  __ \_  ___/  __ \  ___/  ___/  __ \
__/ /  _  ____/     _  /  / / / /_/ /  /   / /_/ / /__ / /__ / /_/ /
/___/  /_/          /_/  /_/  \____//_/    \____/\___/ \___/ \____/ 
                                                                     

""" + RESET)

# 👇 معلومات الأداة
print(CYAN + "Developer : Luki" + RESET)
print(CYAN + "Version   : 1.1.0 (Beta)" + RESET)
print(CYAN + "Admin     : System Control\n" + RESET)

print(CYAN + "1 - IP Lookup")
print("2 - Instagram Search")
print("0 - Exit\n" + RESET)

choice = input(WHITE + "[?] Choose option : " + RESET)


# ---------------- IP TOOL ----------------
if choice == "1":

    ip = input("\nEnter IP Address: ")

    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()

    if data["status"] == "success":
        print(GREEN + "\n=== IP INFORMATION ===\n" + RESET)

        print("IP        :", data.get("query"))
        print("Country   :", data.get("country"))
        print("City      :", data.get("city"))
        print("ISP       :", data.get("isp"))
        print("Org       :", data.get("org"))
        print("Timezone  :", data.get("timezone"))

    else:
        print(RED + "Invalid IP!" + RESET)


# ---------------- INSTAGRAM SEARCH ----------------
elif choice == "2":

    username = input("\nEnter Instagram Username: ")

    print(GREEN + "\nOpening profile...\n" + RESET)

    url = f"https://www.instagram.com/{username}/"

    print("Profile URL:", url)


# ---------------- EXIT ----------------
elif choice == "0":
    print("Bye!")

else:
    print(RED + "Invalid option!" + RESET)
