# tic tac toe
import random

def board(user,computer):
    One = 'X' if 1 in user else ('O' if 1 in computer else 1)
    Two = 'X' if 2 in user else ('O' if 2 in computer else 2)
    Three = 'X' if 3 in user else ('O' if 3 in computer else 3)
    Four = 'X' if 4 in user else ('O' if 4 in computer else 4)
    Five = 'X' if 5 in user else ('O' if 5 in computer else 5)
    Six = 'X' if 6 in user else ('O' if 6 in computer else 6)
    Seven = 'X' if 7 in user else ('O' if 7 in computer else 7)
    Eight = 'X' if 8 in user else ('O' if 8 in computer else 8)
    Nine = 'X' if 9 in user else ('O' if 9 in computer else 9)

    print(f"{One} | {Two} | {Three}")
    print(f"__|___|__")
    print(f"  |   |   ")
    print(f"{Four} | {Five} | {Six}")
    print(f"__|___|__")
    print(f"  |   |   ")
    print(f"{Seven} | {Eight} | {Nine}")

print("Welcome to the tic tac toe!")
user_choices = []
computer_choices = []
win_sets = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
default_numbers = [1,2,3,4,5,6,7,8,9]
while not (default_numbers == []):
    #print board   
    board(user_choices,computer_choices)
    #user selecting field
    number = input("Choose number:")
    number = int(number)
    while(number > 9 or number < 1 or number in user_choices or number in computer_choices):
        print("This number is already filled or it's not in board")
        number = input("Please choose correct number:")
        number = int(number)
    user_choices.append(number)
    default_numbers.remove(number)
    #computer selecting random field
    while(True):
        computer_number = random.randint(0,9)
        if(computer_number not in computer_choices and computer_number in default_numbers and computer_number not in user_choices):
            computer_choices.append(computer_number)
            default_numbers.remove(computer_number)
            break
        else:
            continue
    #wincheck
    for set in win_sets:
        user_result = all(elem in user_choices  for elem in set)
        computer_result = all(elem in computer_choices  for elem in set)
        if user_result:
            print("User Won!")
            exit()
        elif computer_result:
            print("Computer Won!")
            exit()
print("Draft!")

    #I've tried here other way of win check, it did not work, but I'am leaving this cuz it might help me in future ;)
    #user_choices_sorted = []
    #user_choices_sorted = sorted(user_choices)
    #user_choices_sorted = ''.join(user_choices_sorted)

