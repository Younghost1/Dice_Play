import random
import time

def roll_dice():
    """
    Returns the total face value resulting from
    rolling two dice (a number between 2 and 12)
    """
    return random.randint(1, 6) + random.randint(1, 6)


def print_dice(roll):
    """
    Prints a graphical representation of dice rolls
    """
    dice_art = [
        """
         -------
        |       |
        |   •   |
        |       |
         -------
        """,
        """
         -------
        |     • |
        |       |
        | •     |
         -------
        """,
        """
         -------
        | •     |
        |   •   |
        |     • |
         -------
        """,
        """
         -------
        | •   • |
        |       |
        | •   • |
         -------
        """,
        """
         -------
        | •   • |
        |   •   |
        | •   • |
         -------
        """,
        """
         -------
        | •   • |
        | •   • |
        | •   • |
         -------
        """
    ]
    
    dice_rows = []
    
    for i in range(5):
        dice_row = ""
        for dice in roll:
            if 1 <= dice <= 6:
                dice_row += dice_art[dice-1].splitlines()[i] + "  "
            else:
                dice_row += "Invalid Dice Roll" + "  "
        dice_rows.append(dice_row)
    
    for row in dice_rows:
        print(row)


def play_one_game():
    """
    Plays one game of Craps. Returns True if the game
    is won, and False if the game is lost.
    """
    roll = roll_dice()
    print_dice([roll])
    print("You rolled", roll)
    time.sleep(1)
    
    if roll in (7, 11):
        return True
    elif roll in (2, 3, 12):
        return False
    
    point = roll
    print("Your point is", point)
    print()
    time.sleep(1)
    
    while True:
        roll = roll_dice()
        print_dice([roll])
        print("You rolled", roll)
        time.sleep(1)
        
        if roll == point:
            return True
        elif roll == 7:
            return False


def craps():
    """
    Allows the player to repeatedly play a game of Craps. The player
    has an initial bank amount of $1000. They must wager a dollar amount
    prior to the start of the game. The bank balance is increased or
    decreased by the wager amount when the player wins or loses the game,
    respectively.
    """
    print("                ----------------------------")
    print("                Welcome to the Craps program")
    print("                ----------------------------")
    print()
    time.sleep(1)
    
    balance = 1000
    print("Your initial bank balance is $1000.")
    print()
    time.sleep(1)
    
    while True:
        wagerstr = input("What is your wager? ")
        
        try:
            wager = int(wagerstr)
        except ValueError:
            print("Invalid wager amount. Please enter a valid integer.")
            continue
        
        if wager > balance:
            print("Cannot wager more than $", balance)
            continue
        
        print("Okay, let's play.")
        print()
        
        win = play_one_game()
        
        if win:
            print("Congratulations, you win!")
            balance += wager
        else:
            print("Sorry, you lose!")
            balance -= wager
        
        print()
        print("Your new bank balance is $", balance)
        print()
        time.sleep(1)
        
        playagain = input("Do you want to play again? [y/n] ").lower()
        
        if playagain != "y":
            break
    
    print()
    
    if balance < 1000:
        print("Sorry, you lost money. Better luck next time!")
    elif balance > 1000:
        print("Hey, you made some money! Congratulations!")
    else:
        print("At least you broke even...")
    
    print()

if __name__ == "__main__":
    craps()
