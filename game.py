import random 

print('Welcome to the game of rock, paper, and scissors')

options = ['rock', 'paper', 'scissors']

user_input = input('Choose rock, paper, or scissors: ').lower()

while user_input not in options:
    user_input = input('Invalid choice. Please choose rock, paper, or scissors: ').lower()

random_option = random.randint(0, 2)
computer_option = options[random_option]

print(f'Computer chose: {computer_option}')

if user_input == computer_option:
    print("It's a tie!")
elif (user_input == 'rock' and computer_option == 'scissors') or \
     (user_input == 'paper' and computer_option == 'rock') or \
     (user_input == 'scissors' and computer_option == 'paper'):
    print('You have won the game!')
else:
    print('You lost the game.')
