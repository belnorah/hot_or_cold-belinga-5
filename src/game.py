import random
import math

def hot_or_cold():
    # Initialize the game
    print("Welcome to the Hot or Cold game!")
    min_range = 1
    max_range = 100
    target = random.randint(min_range, max_range)
    max_attempts = math.ceil(math.log2(max_range - min_range + 1))
    print(f"Guess the number between {min_range} and {max_range}.")
    print(f"Theoretically, the lowest number of attempts to guess the number is {max_attempts} (optimal guessing).")

    previous_guess = None
    attempts = 0

    while True:
        # Get player's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment attempt counter
        attempts += 1

        # Make sure the number is in the right range
        while guess < min_range or guess > max_range:
            attempts += 1
            print(f"Please enter a number between {min_range} and {max_range}.")
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

        # Check if the guess is correct
        if guess == target:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            print(f"The lowest theoretical number of attempts for this range was {max_attempts}.")
            break

        # Provide feedback
        if previous_guess is None and guess != target:
            print("Keep guessing!")
        else:
            previous_distance = abs(target - previous_guess)
            current_distance = abs(target - guess)

            if current_distance < previous_distance:
                print("Hotter!")
            else:
                print("Colder!")

        # Update the previous guess
        previous_guess = guess

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        hot_or_cold()
    else:
        print("Thanks for playing! Goodbye.")

# Run the game
if __name__ == "__main__":
    hot_or_cold()