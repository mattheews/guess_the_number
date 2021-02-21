import random

def pick_random_number():
    random_number = random.randint(1, 100)
    return random_number

def select_game_difficulty():
    lives = 0
    while lives == 0:
      level_selected = input("Select level\n'easy' or 'hard'?: ")
      if level_selected == "easy":
        lives = 10
      elif level_selected == "hard":
        lives = 5
      if lives == 0:
        print("You specified wrong option.")
    return lives

def check_numbers(random_number, guessed_number):
    if guessed_number > random_number:
        return "To high"
    elif guessed_number < random_number:
        return "To low"
    elif guessed_number == random_number:
        return "You win!"


def check_lives(lives):
    if lives == 0:
        return True
    else:
        return False

### Start Game
print("Welcome in guess the number game!")

end_of_guessing = False
end_of_game = False

while not end_of_game:
  lives = select_game_difficulty()
  number_to_guess = pick_random_number()
  print(number_to_guess)
  while not end_of_guessing:
    guessed_number = int(input("Guess the number between 1 and 100? "))
    guess_check = check_numbers(number_to_guess, guessed_number)
    if guess_check == "You win!":
      print(guess_check)
      end_of_guessing = True
    else:
      lives -= 1
      print(f"Ohh... {guess_check}! Lives remaining: {lives}")
      if check_lives(lives):
        end_of_guessing = True
        print("You run out of lives! Game Over!")
  try_again = input("Try again? y/n: ")
  end_of_guessing = False
  if try_again == "n":
    end_of_game = True
