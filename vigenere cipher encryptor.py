# Bernido, Charles David P. | BSCPE 1-5
# Object Oriented Programming | Lab Exercise 1 - Problem 3

# import modules
import pyfiglet
import colorama
from colorama import Fore, Style
import time

# Create a try-again function to use the program again if the user wants to 
def try_again():
    retry = None
    while retry is None:
        time.sleep(1)
        again = input(Fore.MAGENTA + "\n\t    Do you want to try again? (YES/NO)  ")

        # the program will run again if the user inputted YES
        if again == "Y" or again == "Yes" or again == "YES" or again == "yes":
            retry = str(again)
            main()

        # the program will terminate if the user inputted NO
        if again == "N" or again == "No" or again == "NO" or again == "no":
            time.sleep(0.5)
            print(Fore.CYAN + "\t    [Program will be terminated..............]")

            time.sleep(1.5)
            print("\n")
            print(Fore.GREEN + "\033[1m-" * 140 + '\033[0m')
            print(" ")

            lab = pyfiglet.figlet_format("   THANK YOU !!   ", font = "banner3",  width = 140, justify = "center")
            print(Style.BRIGHT + Fore.GREEN + lab)
            exit()
        else:
            print(Fore.RED + "\t    [ERROR] Please choose either YES or NO only.")

# create variable 'letters' that contain A-Z letters
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create encryption function

# Use pyfiglet formatting to "Lab. Exercise No. 1"
# format introductory message

# insert time delay

# define main function
    # ask the user to input the message and key
    # accept only uppercase letters and no spaces
    # call encrypt function
    # display cipher text

# call main function

# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS
