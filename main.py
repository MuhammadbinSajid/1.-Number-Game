import random #importing module
playing = True #initialise
number  = str(random.randint(10,20)) #random in-built function

print("I will generate a number from 10 to 20, and you have to guess the number one digitat a time.")
print("The game ends when you get 1 hero!")
#iterate loop till the conition is true
while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was",number)
        break
    else:
        print("Your guess is'nt quite right, try again. \n")