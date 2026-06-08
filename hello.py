from colorama import init, Fore, Style
from pymupdf import message
init()

def display():
    message = f"{Fore.GREEN}Bonjour les {Fore.CYAN}FI1{Style.RESET_ALL}"
    print(message)


if __name__ == "__main__":
    display()