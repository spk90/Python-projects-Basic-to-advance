
import random
print ("Welcome to this number guessing game")

question = input("Do you want to start this game? Enter yes or no. Enter = ")

randomnum = random.randint(1,10)

if question != ('yes'):
    quit()
print("welcome to this game")

answer = input("Enter a number between 1 to 10 :")
if answer == randomnum:
    print("You have won the lottery")
else:
    print("better luck next time  " + "The correct answer is " +  str(randomnum))
    
