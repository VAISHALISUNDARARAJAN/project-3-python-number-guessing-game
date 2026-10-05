import random


def choose_difficulty():
    print("\n===== SELECT DIFFICULTY =====")
    print("1. Easy   (1-20, 7 attempts)")
    print("2. Medium (1-50, 6 attempts)")
    print("3. Hard   (1-100, 5 attempts)")

    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            return 20, 7, "Easy"

        elif choice == "2":
            return 50, 6, "Medium"

        elif choice == "3":
            return 100, 5, "Hard"

        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


def play_game():
    maximum, max_attempts, difficulty = choose_difficulty()

    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\n===== {difficulty.upper()} MODE =====")
    print(f"I have selected a number between 1 and {maximum}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > maximum:
                print(f"Please enter a number between 1 and {maximum}.")
                continue

            attempts += 1

            if guess == secret_number:
                score = max_attempts - attempts + 1

                print("\nCongratulations! You guessed the correct number!")
                print(f"Attempts used: {attempts}")
                print(f"Your score: {score}")
                return

            elif guess < secret_number:
                print("Too Low!")

            else:
                print("Too High!")

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")
    print("Better luck next time!")


def main():
    print("===== NUMBER GUESSING GAME =====")

    while True:
        play_game()

        choice = input("\nDo you want to play again? (y/n): ").strip().lower()

        if choice == "y":
            print("\nStarting a new game...")

        elif choice == "n":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Game ended.")
            break


main()
