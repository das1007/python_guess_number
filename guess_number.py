from random import randint


def check_answer(guess, answer):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        return print("Too high.")
    elif guess < answer:
        return print("Too low.")
    else:
        return print(f"You got it! The answer was {answer}.")


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        check_answer(guess, answer)


game()
