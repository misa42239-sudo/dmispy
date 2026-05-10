import requests
import os
import time
import sys
import asyncio
from colorama import Fore, Style, init
from telethon import TelegramClient

# Initialize colorama
init(autoreset=True)

# TELEGRAM API CREDENTIALS (GET THEM FROM my.telegram.org)
# LEAVE THESE EMPTY IF UPLOADING TO GITHUB!
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{Fore.RED}
    ██████╗ ███╗   ███╗██╗███████╗██████╗ ██╗   ██╗
    ██╔══██╗████╗ ████║██║██╔════╝██╔══██╗╚██╗ ██╔╝
    ██║  ██║██╔████╔██║██║███████╗██████╔╝ ╚████╔╝ 
    ██║  ██║██║╚██╔╝██║██║╚════██║██╔═══╝   ╚██╔╝  
    ██████╔╝██║ ╚═╝ ██║██║███████║██║        ██║   
    ╚═════╝ ╚═╝     ╚═╝╚═╝╚══════╝╚═╝        ╚═╝   
    {Fore.WHITE}      >> Advanced OSINT Reconnaissance Framework <<
    {Fore.YELLOW}          Created by: Wolf (Dmimaks)
    """)

def progress_bar(text):
    print(f"{Fore.YELLOW}[*] {text}", end="")
    for i in range(20):
        time.sleep(0.05)
        sys.stdout.write(f"{Fore.RED}█")
        sys.stdout.flush()
    print(f" {Fore.GREEN} DONE!")

async def check_telegram(username):
    progress_bar("Bypassing Telegram Privacy...")
    if API_ID == 'YOUR_API_ID':
        print(f"\n{Fore.RED}[!] ERROR: Please set your API_ID and API_HASH in the script!")
        return

    async with TelegramClient('osint_session', API_ID, API_HASH) as client:
        try:
            entity = await client.get_entity(username)
            print(f"\n{Fore.GREEN}[+] TELEGRAM PROFILE FOUND:")
            print(f"{Fore.WHITE}Full Name: {entity.first_name} {entity.last_name if entity.last_name else ''}")
            print(f"{Fore.WHITE}User ID: {Fore.YELLOW}{entity.id}")
            print(f"{Fore.WHITE}Username: @{entity.username}")
            print(f"{Fore.WHITE}Is Bot: {entity.bot}")
            print(f"{Fore.WHITE}Scam Flag: {entity.scam}")
            print(f"{Fore.WHITE}Verified: {entity.verified}")
        except Exception as e:
            print(f"\n{Fore.RED}[-] Telegram target not found or API error.")

def scan_socials(target):
    progress_bar("Scanning Global Databases...")
    platforms = {
        "Instagram": f"https://www.instagram.com/{target}/",
        "Twitter": f"https://twitter.com/{target}",
        "Steam": f"https://steamcommunity.com/id/{target}",
        "GitHub": f"https://github.com/{target}",
        "Twitch": f"https://www.twitch.tv/{target}",
        "Roblox": f"https://www.roblox.com/user.aspx?username={target}"
    }
    
    print(f"\n{Fore.CYAN}[*] SEARCH RESULTS FOR: {target}\n")
    for name, url in platforms.items():
        try:
            r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] MATCH: {name} -> {url}")
            else:
                print(f"{Fore.WHITE}[-] NOT FOUND: {name}")
        except:
            print(f"{Fore.YELLOW}[!] Connection Error on {name}")

def main_menu():
    while True:
        clear()
        banner()
        print(f"{Fore.YELLOW}[1] {Fore.WHITE}Full Social Media Scan (Nick)")
        print(f"{Fore.YELLOW}[2] {Fore.WHITE}Telegram Deep Probe (API)")
        print(f"{Fore.YELLOW}[3] {Fore.WHITE}GitHub Intelligence Scan")
        print(f"{Fore.YELLOW}[0] {Fore.WHITE}Exit Framework")
        
        choice = input(f"\n{Fore.RED}DmiSpy > {Fore.WHITE}")
        
        if choice == '1':
            target = input(f"{Fore.YELLOW}Enter target nickname: ")
            scan_socials(target)
            input(f"\n{Fore.CYAN}Press Enter to return...")
        
        elif choice == '2':
            target = input(f"{Fore.YELLOW}Enter Telegram @username (without @): ")
            asyncio.run(check_telegram(target))
            input(f"\n{Fore.CYAN}Press Enter to return...")

        elif choice == '3':
            target = input(f"{Fore.YELLOW}Enter GitHub username: ")
            print(f"{Fore.GREEN}[+] Profile: https://github.com/{target}")
            input(f"\n{Fore.CYAN}Press Enter to return...")
            
        elif choice == '0':
            print(f"{Fore.RED}Terminating session...")
            break

if __name__ == "__main__":
    main_menu()