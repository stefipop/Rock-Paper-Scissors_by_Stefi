import random
from colorama import Fore, Style

print("Hello, what's your name?")
name = input("If you want to remain anonymous, just write X: ")
if name == "x" or name == "X":
    name = "00X"
print(f"Hi {name}, do you having trouble making a decision?")
print("Let's see what fate has in store for you...")

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input(Fore.LIGHTGREEN_EX + "Choose [r]ock, [p]aper or [s]cissors and press Enter: ").lower()
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print(Fore.LIGHTMAGENTA_EX + "Invalid Input. Try again...")
        continue

    # Modify the computer move selection based on the biased strategy
    # computer_random_move = random.choices([1, 2, 3], weights=[0.4, 0.3, 0.3])[0]
    computer_random_move = random.randint(1, 3)

    win = ["You win!", "Yesss, the right choice for you!", "You aced it!", "You nailed it!",
           "Victory for you!", "You've unlocked the secret cheat code for winning in life!",
           "Victory dances were invented just for you! Get grooving!",
           "You're a winner in the game of life, and your score is off the charts!"]
    draw = ["Balanced opportunity", "Split chance", "Fifty-fifty", "Dead heat", "No clear winner", "Draw"]
    lose = ["Oops! Better luck next time, champ!", "Close, but no victory dance this time!",
            "You're one step closer to being an expert loser!", "Remember, losing builds character... and resilience!",
            "No win today, but your wit and charm remain undefeated!",
            "Chin up, sunshine! Your winning streak is hibernating!"]
    comp_said = ["Behold! The computer's mystical choice is:", "The computer's crystal ball pointed to:",
                 "In a stunning twist, the computer settled on:",
                 "The computer's random generator whispered the secret word:",
                 "The computer's high-tech AI whispered in binary code:",
                 "Breaking news! The computer's decision is:"]
    random_item = random.choice(comp_said)
    computer_move = ""
    if computer_random_move == 1:
        computer_move = rock
    elif computer_random_move == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(Fore.LIGHTBLUE_EX + f"{random_item} {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        random_item = random.choice(win)
        print(Fore.GREEN + random_item)
    elif player_move == computer_move:
        random_item = random.choice(draw)
        print(Fore.YELLOW + random_item)
    else:
        random_item = random.choice(lose)
        print(Fore.RED + random_item)

    play_again = input(Style.RESET_ALL + "Do you want to play again? ( y / n ) ").lower()
    if play_again != "y":
        break
