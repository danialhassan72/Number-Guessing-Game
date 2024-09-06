import random
def guess_checker(guess,answer,lives):
    """it will see the user's guess against the answer and returnthe updated lives."""
    if guess > answer:
        print("Too High.")
        return lives - 1
    elif guess < answer:
        print("Too Low.")
        return lives - 1
    else:
        print("you got it right!")
        return 0

def set_difficulty():
    """Set difficulty level and return the number of lives"""
    level = input("choose a difficulty. Type 'easy' or 'hard':").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("invalid input. setting difficulty to 'easy' by default.")
        return 10

def play_game():
    """Main function to play the number guessing game."""
    print("welcome to the number of guessing game!")
    print("I m thinking of a number between 1 and 100")

    answer = random.randint(1, 100)
    # for cheating purposes
    print(f"Pssst, the correct answer is {answer}")

    lives = set_difficulty()
    guess = 0

    while guess != answer and lives > 0:
        print(f"you have {lives} attempts remaining to guess the number.")

        try:
            guess = int(input("Make a guess:"))
            lives = guess_checker(guess,answer,lives)
        except ValueError:
            print("invalid input. please enter an integer.")

        if lives == 0 and guess != answer:
            print(f"you have run out of guessess. The correct answer was {answer}.")
def play_again():
    user_input = input("do you  want to play again? type yes or no: \n".lower())
    if user_input == "yes":
        play_game()
    else:
        "thank you for playing the number guessing game!"
def main ():
    play_game()
main()
play_again()
