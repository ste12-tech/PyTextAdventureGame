from time import sleep
import random
#importing sleep and random
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

room = 'starting_room'
coins = 0
game_running = True
#set up variables for the game
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("Welcome to the Adventure Game!")
sleep(1)
next_room = input(f"You are currently in the {room} with {coins} coins. would you like to go to the main hall (enter 1) or the corridor? (enter 2) ")
while next_room != '1' and next_room != '2':
    print("Are you sure you pressed the right key? Please try again.")
    next_room = input(f"please try again. You are still in the {room} with {coins} coins. would you like to go to the main hall (enter 1) or the corridor? (enter 2) ")
#move on to next room based on user input
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if next_room == '1':
    room = 'main_hall'
    print(f"You have entered the {room}.")
elif next_room == '2':
    room = 'corridor'
    print(f"You have entered the {room}.")
#which room the player has entered based on their input
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def gnfc(coins):
    game1 = 10
    sleep(1)
    v1 = input("would you like difficulty 1 2 or 3? ")
    if v1 == '1':
        num1 = random.randint(1, 10)
        sleep(1)
        print("You have chosen difficulty 1. You will have to guess the number between 1 and 10 each time you dont get it 1 point gets deducted from 10.")
        guess1 = int(input("try to guess the number between 1 and 10: "))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        while guess1 != num1:
            sleep(1)     
            if guess1 < num1:
                game1 -= 1
                print("Your guess is too low. Try again.")
            elif guess1 > num1:
                print("Your guess is too high. Try again.")
                game1 -= 1
                
            guess1 = int(input("Try to guess the number between 1 and 10: "))
        print("Congratulations! You guessed the number correctly.")
        coins = coins + game1
        print(f"You have gained {game1} coins and now have {coins} coins.")
        return coins
    elif v1 == '2':
            num1 = random.randint(1, 10)
            sleep(1)
            print("You have chosen difficulty 2. You will have to guess the number between 1 and 10 each time you dont get it 1 point gets deducted from 10.")
            guess1 = int(input("try to guess the number between 1 and 10: "))
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            while guess1 != num1:
                sleep(1)     
                if guess1 < num1:
                    game1 -= 2
                    print("Your guess is too low. Try again.")
                elif guess1 > num1:
                    print("Your guess is too high. Try again.")
                    game1 -= 2
                    
                guess1 = int(input("Try to guess the number between 1 and 10: "))
            print("Congratulations! You guessed the number correctly.")
            coins = coins + game1
            print(f"You have gained {game1} coins and now have {coins} coins.")
            return coins
    if v1 == '3':
            num1 = random.randint(1, 10)
            sleep(1)
            print("You have chosen difficulty 1. You will have to guess the number between 1 and 10 each time you dont get it 1 point gets deducted from 10.")
            guess1 = int(input("try to guess the number between 1 and 10: "))
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            while guess1 != num1:
                sleep(1)     
                if guess1 < num1:
                    game1 -= 3
                    print("Your guess is too low. Try again.")
                elif guess1 > num1:
                    print("Your guess is too high. Try again.")
                    game1 -= 3
                    
                guess1 = int(input("Try to guess the number between 1 and 10: "))
            print("Congratulations! You guessed the number correctly.")
            coins = coins + game1
            print(f"You have gained {game1} coins and now have {coins} coins.")
            return coins
    coins = gnfc(coins)
    
    
coins = gnfc(coins)
