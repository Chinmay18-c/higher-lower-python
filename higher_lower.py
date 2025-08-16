import random
import os
from colorama import Fore, Style, init
from data import data

init(autoreset=True)

def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    return guess == "b"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def game():
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        clear()
        print(f"\nCompare A: {Fore.CYAN}{format_data(account_a)}{Style.RESET_ALL}")
        print("VS")
        print(f"Against B: {Fore.MAGENTA}{format_data(account_b)}{Style.RESET_ALL}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(Fore.GREEN + f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(Fore.RED + f"Sorry, that's wrong. Final score: {score}")

game()
