import random

# Resources
user_input_list = ["Rock", "Paper", "Sisscors", "1", "2", "3"]
computer_list = ["Rock", "Paper", "Sisscors"]


def get_input():
    while True:
        the_input = input("\nInsert your command : ").strip()
        if the_input not in user_input_list:
            print("\nPlease Enter an Valid Command!!\n")
            continue
        else:
            break
    return the_input


def generate_computer_input():
    the_computer_choice = random.choice(computer_list)
    print(f"\nComputer: {the_computer_choice}")
    return the_computer_choice


def check_who_won(user_input, computer_input):
    if user_input != computer_input:
        if user_input == "Rock" and computer_input == "Sisscors":
            return "yes"
        elif user_input == "Paper" and computer_input == "Rock":
            return "yes"
        elif user_input == "Sisscors" and computer_input == "Paper":
            return "yes"
        else:
            return "no"
    else:
        return "Draw"


def wining_messege(winner, final=None):
    # print(f"\nThe winner ouf this round is {winner}\n")
    if final:
        print(f"\nThe winner ouf this game is {winner}\n")
    else:
        print(f"The winner ouf this round is {winner}\n")


def decide_who_won(user_score, computer_score):
    if user_score > computer_score:
        return "user"
    if user_score < computer_score:
        return "computer"
    else:
        return "no_one"


def user_winner_declaration(game_winner):
    if game_winner == "user":
        wining_messege("User", True)
    if game_winner == "computer":
        wining_messege("Computer", True)
    else:
        print("The game is a draw.")


def Wanna_play_again():
    while True:
        the_command = input("Wanna play again? (Y/N) :").lower().strip()
        if the_command == "y":
            return "yes"
        if the_command == "n":
            return "n"
        else:
            print("\nInvalid Input!!")
            continue
