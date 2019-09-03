import sys, os

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def check_version(version):
    assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

def print_color(str):
    str += "\033[0m" #set it back to white when we are done
    print(str
        .format(
            white = '\033[0m'
            ,black = '\033[30m'
            ,red = '\033[31m'
            ,green = '\033[32m'
            ,yellow = '\033[33m'
            ,blue = '\033[34m'
            ,magenta = '\033[35m'
            ,cyan = '\033[36m'
            ,brightBlack = '\033[90m'
            ,brightRed = '\033[91m'
            ,brightGreen = '\033[92m'
            ,brightYellow = '\033[93m'
            ,brightBlue = '\033[94m'
            ,brightMagenta = '\033[95m'
            ,brightCyan = '\033[96m'
        ))