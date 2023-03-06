import random
def guess(x):
    random_number = random.randint(1, x)
    user_guess = None
    guess_count = 0
    while user_guess!=random_number:
        user_guess = int(input(f"Guess the number between 1 to {x}  -  "))
        guess_count+=1
        if user_guess > random_number:
            print("Sorry,Its too high. Try Again")
        elif user_guess < random_number:
            print("Sorry,Its too low. Try Again")
    print(f"Congrats..You Guess The Correct Number in {guess_count} times.")

guess(101)