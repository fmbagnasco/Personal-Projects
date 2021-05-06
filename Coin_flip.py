#program for a coin flip game

import random

#welcome message
print("Welcome to Coin Flip and Dice Roll!")

#set up global variables
wins = 0
plays = 0
game = True

while game:
    #set up of the computer variables
    coin = random.randint(0,1)
    dice = random.randint(1,6)

    #translate coin in str
    if coin == 0:
        coin = "Head"
    elif coin == 1:
        coin = "Tail"

    #ask which game
    print("Which game would you like to play?")
    print("Write Coin for Coin Flip.")
    print("Write Dice for Dice Roll.")
    game = input("--> ")

    while game != "Coin" and game != "Dice":
        print("Invalid input. Remember to Capitalize your choice.")
        print("Try again:")
        game = input("--> ")

    if game == "Coin":
        #prompt to select an input and set up user variable
        print("Please, select Head or Tail by writing your choice below:")
        user_coin = input("--> ")

        #verify user input
        while user_coin != "Head" and user_coin != "Tail":
            print("Invalid input. Remember to Capitalize your choice.")
            print("Try again:")
            user_coin = input("--> ")

        print("Great choice!")

        #show what the computer chooses
        print("The coin lands on... " + coin + "!")
            
        if user_coin == coin:
            print("You guessed right! You won!")
            wins += 1
            plays += 1
        else:
            print("Your guess was wrong! You lost!")
            plays += 1

        #Updated count
        print("Games played: " + str(plays))
        print("Games won " + str(wins))
        print("Your success rate is " + str(100 * wins / plays) + "%")

        #ask play again
        print("Do you want to play again? Y/N")
        play_again = input("--> ")

        while play_again != "Y" and play_again != "N":
            print("Invalid input. Remember to Capitalize your choice.")
            print("Try again:")
            play_again = input("--> ")

        if play_again == "N":
            game = False
        elif play_again == "Y":
            game = True

    if game == "Dice":
        #prompt to select an input and set up user variable
        print("Please, select a number between 1 and 6:")
        user_dice = int(input("--> "))

        #verify user input
        while (user_dice < 1) or (user_dice > 6):
            print("Invalid input.")
            print("Try again:")
            user_dice = int(input("--> "))

        print("Great choice!")

        #show what the computer chooses
        print("The computer rolls: " + str(dice) + "!")
            
        if user_dice == dice:
            print("You guessed right! You won!")
            wins += 1
            plays += 1
        else:
            print("Your guess was wrong! You lost!")
            plays += 1

        #Updated count
        print("Games played: " + str(plays))
        print("Games won " + str(wins))
        print("Your success rate is " + str(100 * wins / plays) + "%")

        #ask play again
        print("Do you want to play again? Y/N")
        play_again = input("--> ")

        while play_again != "Y" and play_again != "N":
            print("Invalid input. Remember to Capitalize your choice.")
            print("Try again:")
            play_again = input("--> ")

        if play_again == "N":
            game = False
        elif play_again == "Y":
            game = True

#final message
print("Thank you for playing Coin Flip and Dice Roll!")