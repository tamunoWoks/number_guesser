"""
Guess the Number Game
---------------------
The computer selects a random number between 1-20,
and the player has 6 attempts to guess it.
After each guess, the computer provides feedback
(too high/too low) until the player guesses correctly.
"""

# Import only the randint function from random module
from random import randint

# Generate a random number between 1 and 20
secret_number = randint(1, 20)

# Display game instructions
print('I am thinking of a number between 1 and 20.')
