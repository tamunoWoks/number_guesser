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

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
  print('Take a guess.')
  guess = int(input('>'))

  # Evaluate player guess
  if guess < secret_number:
    print('Your guess is too low.')
  elif guess > secret_number:
    print('Your guess is too high.')
  else:
    break # This condition is the correct guess!

# After the loop ends, check why it ended:
if guess == secret_number:
  print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
  print('Nope. The number was ' + str(secret_number))
