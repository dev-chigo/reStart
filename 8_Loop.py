"""
A script of while loop
"""
import random
print("Welcome to Guess the Number! \nThe rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False #this variable
while isGuessRight !=True: #while loop will repeat the code inside the loop until the number is guessed correctly, which is represented by the condition isGuessRight != True
    guess = input("Guess a number between 1 and 10: ") #input variable where the user inserts the number
    if int(guess) == number: #this allows the variable guess input to be an integer and if the number matches 1
        print("You guess {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))