import random

randomnum = random.randint(7, 9)

name = input("What is your name? ")
print("Welcome to the game of adventure " + name)

answer = input('What do you choose to do? Go left or Right: ').lower()

if answer == "left":
    print("OHOHOOOO you chose left, now you have two options: Cross the river here or go around.")
    ans2 = input("Choose 'river' or 'go around': ").lower()

    if ans2 == "river":
        print("You are in the endgame now! Congratulations!")
    elif ans2 == "go around":
        print("Choose a number between 7, 8, 9.")
        ans3 = input("Choose a number: ")

        if ans3.isdigit() and int(ans3) == randomnum:
            print("You have won the game!")
        else:
            print("Incorrect number! You lost the game.")
    else:
        print("Invalid choice! You lost the game.")
        
elif answer == 'right':
    print("You chose right! There’s a hidden treasure chest ahead.")
    # Add more options or outcomes for this choice
    ans_right = input("Do you want to open the chest? (yes/no): ").lower()
    if ans_right == "yes":
        print("The chest was full of gold! You win!")
    elif ans_right == "no":
        print("You chose wisely. No traps, but no treasure either.")
    else:
        print("That's not a valid answer. You lose!")
    
else:
    print("Invalid direction! You lost the game.")
