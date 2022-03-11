from zplasty import Zplasty
from colorama import Fore, Style

if __name__ == '__main__':
    print(Fore.MAGENTA + r"""

  ______     _____  _           _         
 |___  /    |  __ \| |         | |        
    / /_____| |__) | | __ _ ___| |_ _   _ 
   / /______|  ___/| |/ _` / __| __| | | |
  / /__     | |    | | (_| \__ \ |_| |_| |
 /_____|    |_|    |_|\__,_|___/\__|\__, |
                                     __/ |
                                    |___/ 

    """)
    print(Fore.BLUE + "https://github.com/tkruer/Z-Plasty")
    print(Style.BRIGHT + "Let's Get Calculating! 🚀")
    print()
    print()
    zplasty = Zplasty()
    zplasty.start()