import random
num = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 - 50: "))
    attempts += 1
    if guess > num:
        print("Your guess is too high!")

    elif guess < num:
        print("Your guess is too low!")

    else:
        print("Your guess is correct!")
        print(f"You got it after {attempts} attempts")
        break