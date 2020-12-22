import random as r

user_options = ['ROCK', 'PAPER', 'SCISSORS']
PC_score = 0
Player_score = 0


while True:
    user_choice = input("Choose rock, paper or scissors! ").upper()
    if user_choice in user_options:
        PC_choice = user_options[r.randint(0, 2)]
        print(PC_choice)
        if PC_choice == user_choice:
            print("This was a draw!")
        elif PC_choice == user_options[0] and user_choice == user_options[1]:
            Player_score = + 1
            print("Player won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
        elif PC_choice == user_options[0] and user_choice == user_options[2]:
            PC_score = + 1
            print("PC won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
        elif PC_choice == user_options[1] and user_choice == user_options[0]:
            PC_score = + 1
            print("PC won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
        elif PC_choice == user_options[1] and user_choice == user_options[2]:
            Player_score = + 1
            print("Player won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
        elif PC_choice == user_options[2] and user_choice == user_options[0]:
            Player_score = + 1
            print("Player won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
        else:
            PC_score = + 1
            print("PC won! Score is now {} for PC and {} for player".format(PC_score, Player_score))
    else:
        print("INVALID CHOICE! Try again.")