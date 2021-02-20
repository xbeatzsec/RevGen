#!/usr/bin/python3

# This is my first tool for pentesting and I hope to in the future do more scripts and pentesting tools

# MMMMMMMMMMMMMMMXd,....'lKWMMMMMMMMMMMMMM
# MMMMMMMMMMMMMNx::okxoc::;oXMMMMMMMMMMMMM
# MMMMMMMMMMMW0:;xNMMXOdodo;;kWMMMMMMMMMMM
# MMMMMMMMMMWO;:KMMMMKxdoool,'xWMMMMMMMMMM
# MMMMMMMMMMO,cXMMMMMKxdolooc'.xWMMMMMMMMM
# MMMMMMMMM0;;k0Oxxddc;,,,,;::''kWMMMMMMMM
# MMMMMMMMK; ....;,,,,,,,,,'.   'OMMMMMMMM
# MMMMMMMMx.    cXWWW0x0NWNo.    lWMMMMMMM
# MMMMMMMMXl.   .xWMMX0KWM0'   .:0MMMMMMMM
# MMMMMMMMNk,    .oOXNNX0d'    .xXWMMMMMMM
# MMMMMW0o,.        .''..        'lOWMMMMM
# MMMMWk. .',,,,,,,,,,,,,,,,,,,,,. .oNMMMM
# MMMMO'  lNWWWWWWNXOOOOXNWWWWWWWx. .xWMMM
# MMMK;   lWMMMMMXo'.  .'oKMMMMMMx.  'OWMM
# MMNc    cNMMMMNl.      .cNMMMMWd.   ;KMM
# MMO.    cNMMMMNl,l;..;l,lNMMMMWo    .dWM
# MM0,    :XMMMMMO,......'OMMMMMWo    .kMM
# NNXk'   ;XMMMMMN0l'..'l0NMMMMMNl   .dXNN
# olll:'. .dkkkkkkkxddddxkkkkkkkx, .';cllo
# NNNNNN0,.';;,,;,,,,,;,,,,,,,;,,..kNNNNNN
# MMMMMMNl........................;XMMMMMM

# Script made by Hernani
# Version 1.0


# Imports

import os
import time
from payloads import payloads
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\u001b[37m'


# os.system("clear")
print("" + bcolors.WARNING)
banner = """


 ---------------------------------------------------

 ██████╗░███████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗
 ██╔══██╗██╔════╝██║░░░██║██╔════╝░██╔════╝████╗░██║
 ██████╔╝█████╗░░╚██╗░██╔╝██║░░██╗░█████╗░░██╔██╗██║
 ██╔══██╗██╔══╝░░░╚████╔╝░██║░░╚██╗██╔══╝░░██║╚████║
 ██║░░██║███████╗░░╚██╔╝░░╚██████╔╝███████╗██║░╚███║
 ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝

 RevGen 1.0

 Coded by Hernani

 ---------------------------------------------------

 This script generate the most commun commands / code to spawn a shell.
 Any problem or bugs please let me know :D

"""


print(banner)
print("" + bcolors.OKGREEN)

ip = str(input("IP -> "))

print("")
port = str(input("Port -> "))


menu = """
1 -> Python
2 -> Bash TCP
3 -> Perl
4 -> PHP
5 -> Netcat
"""
print(menu)
print("")
try:
    option = int(input("Option: "))
    if option > 5:
        sys.exit()
except:
    error = """
    Select a valid option
    """
    print(error)
    sys.exit()

payloads(ip, port, option)
