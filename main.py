import funtions

# Introduction
print("Welcome to the game of ROCK PAPER SISSCORS.This is my third python project.\nGame rule : There will be total of 7 trial .Winner of each trial will awarded one point.\nAfter 7 trials, whoever has the most score will win.\n\nBEST OF LUCK!!!\n\n")

# The point count portion
user_score = 0
computer_score = 0

# The main gameloop
input("Press Enter to start the game... ...")
while True:
    for trial in range(6):
        print(
            f"\nUeser score : {user_score}\nComputer score : {computer_score}")
        print("\n1.Rock\n2.Paper\n3.Sisscors\n")
        user_input = funtions.get_input()
        # input_is_valid = funtions.check_for_input_validity(user_input)
        computer_input = funtions.generate_computer_input()

        user_won = funtions.check_who_won(user_input, computer_input)
        if user_won == "yes":
            funtions.wining_messege("User")
            user_score += 1
        elif user_won == "no":
            funtions.wining_messege("Computer")
            computer_score += 1
        else:
            funtions.wining_messege("Draw")

    game_winner = funtions.decide_who_won(user_score, computer_score)

    funtions.user_winner_declaration(game_winner)
    again_play = funtions.Wanna_play_again()
    if again_play:
        user_score = 0
        computer_score = 0
        continue
    else:
        break
