from data import data, higher_lower_logo, vs
from replit import clear
import random


def get_option():
    """Returns an option."""
    option = random.choice(data)
    return option


def more_followers(A, B):
    """Returns the follower count of who has more followers out of A and B."""
    if A["follower_count"] > B["follower_count"]:
        return A
    return B


def compare(user_guess, option):
    if user_guess == option:
        return True
    return False


def higher_lower():
    score = 0
    game_over = False
    while not game_over:

        print(higher_lower_logo)

        if score == 0:
            option_A = get_option()
        else:
            print(f"You're right! Your score: {score}")
            option_A = option_B
        print(
            f"Compare A: {option_A['name']}, {option_A['description']}, from {option_A['country']}")

        print(vs)

        option_B = get_option()
        print(
            f"Compare B: {option_B['name']}, {option_B['description']}, from {option_B['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == 'a':
            guess = option_A
        elif guess == 'b':
            guess = option_B

        winner = more_followers(option_A, option_B)

        clear()

        if compare(guess, winner):
            score += 1
        else:
            game_over = True
            print(f"Sorry, that's wrong! Final score: {score}")


while input("Type 'y' to play a game of 'Higher Lower' : ") == 'y':
    higher_lower()

print("\nBye...")
