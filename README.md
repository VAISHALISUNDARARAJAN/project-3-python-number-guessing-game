# Python Number Guessing Game

A beginner-friendly number guessing game developed using Python.

## Features

- Generates a random number using Python's random module
- Provides Easy, Medium and Hard difficulty levels
- Gives "Too High" and "Too Low" hints
- Counts the number of attempts
- Displays the final score
- Provides different number ranges and attempt limits
- Allows the player to restart the game
- Handles invalid input safely

## Technologies Used

- Python
- Python Random Module

## Difficulty Levels

| Difficulty | Number Range | Attempts |
|------------|--------------|----------|
| Easy | 1 - 20 | 7 |
| Medium | 1 - 50 | 6 |
| Hard | 1 - 100 | 5 |

## How to Run

1. Make sure Python is installed on your computer.
2. Open `number_guessing_game.py` using Python IDLE or any Python IDE.
3. Run the program.
4. Select a difficulty level.
5. Enter your guesses.
6. Follow the hints provided by the program.
7. Choose whether to play again after the game ends.

## Scoring

The score depends on the number of attempts used.

The fewer attempts used to guess the correct number, the higher the score.

## Example

```text
===== NUMBER GUESSING GAME =====

===== SELECT DIFFICULTY =====
1. Easy   (1-20, 7 attempts)
2. Medium (1-50, 6 attempts)
3. Hard   (1-100, 5 attempts)

Enter your choice (1-3): 1

===== EASY MODE =====
I have selected a number between 1 and 20.
You have 7 attempts to guess it.

Enter your guess: 10
Too Low!
Attempts remaining: 6

Enter your guess: 17
Too High!
Attempts remaining: 5

Enter your guess: 14

Congratulations! You guessed the correct number!
Attempts used: 3
Your score: 5
