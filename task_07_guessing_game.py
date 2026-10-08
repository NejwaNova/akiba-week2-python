secret_number = 42
attempts = 0
maximum_attempts = 5

print("===== NUMBER GUESSING GAME =====")
print("Guess the secret number.")
print(f"You have {maximum_attempts} attempts.")

while attempts < maximum_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"Congratulations!")
        print(f"You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    remaining_attempts = maximum_attempts - attempts
    if remaining_attempts > 0:
        print(f"Attempts remaining: {remaining_attempts}")
    else:
        print("Game Over!")
        print(f"The secret number was {secret_number}.")