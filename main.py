#Kent Tran
#September 2, 2025
#Lab 2 - Three Card Monte

import check_input
import random

def get_users_bet(money): 
    """shows user current money and gets a bet amount
        Args:
            money(integer): the amount of money user has to play with
    
        Returns:
            returns the bet value

        Raises:
            Error: If the bet input is not an integer, or if it's out of range
    """
    print("You have $" + str(money))

    bet = check_input.get_int_range("How much do you want to bet? ", 1, money)
    return bet

def get_users_choice(): 
    """prints the card and gets an input for a choice
        Args:
    
        Returns:
            returns the users choice

        Raises:
            Error: If the choice is out of range
    """
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")
    print("|  1  | |  2  | |  3  |")
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

    choice = check_input.get_int_range("Find the queen ", 1, 3)
    return choice

def display_queen_loc(queen_loc):
    """displays the queen location after the user makes a guess
        Args:
            queen_loc(int): location of the queen card
    
        Returns:
            None

        Raises:
            Error: none
    """
    print("+-----+ +-----+ +-----+")
    print("|     | |     | |     |")

    if queen_loc == 1:
        print("|  Q  | |  K  | |  K  |")
    elif queen_loc == 2:
        print("|  K  | |  Q  | |  K  |")
    else:
        print("|  K  | |  K  | |  Q  |")
    
    print("|     | |     | |     |")
    print("+-----+ +-----+ +-----+")

def main():
    """runs the game
        Args:
            none
    
        Returns:
            none

        Raises:
            Error: none
    """
    print("-Three Card Monte-")
    print("Find the Queen to double your bet!")

    money = 100

    while money > 0:
        queen_location = random.randint(1, 3) #gives the queen a random position

        bet = get_users_bet(money)
        user_choice = get_users_choice()
        display_queen_loc(queen_location)

        if user_choice == queen_location:
            money += bet
            print("You got lucky this time...")
        else:
            print("Sorry... you lose.")
            money -= bet

        if money <= 0: #only if the player runs out of money
            print("You're out of money. Beat it loser!")
            break

        play_again = input("Play again? (Y/N): ")
        if play_again.upper() == "N":
            break

main()
