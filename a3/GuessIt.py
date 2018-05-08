#Devroop Banerjee
#V00837868
#Deepti Yadawad
#V00838513

# This is a guess the number game.
import random
print('Hey! What\'s your name?')
Name = input()

#Generates random number between 1 and 100
number = random.randint(1, 100)
print('Well, ' + Name + ', I am thinking of a number between 1 and 100.')
GuessNum = 0
TryNum = 0

#It'll keep looping till the user guesses the correct number
while GuessNum != number:
#Increments the number of tries    
    TryNum = TryNum + 1
    print('Take a guess between 1 and 100')
#Takes input from user    
    GuessNum = input()
#Gives an error message if the number input is negative or not a number   
    if (not GuessNum.isnumeric()):
        print (" No! That's not what I asked for! Please enter a proper number")
        continue
    GuessNum = int(GuessNum)
#Checking for how close the number guessed is to the value generated and outputting hint messages accordingly    
    if((GuessNum == 0)or (GuessNum > 100)):
        print('...I said the range is between 1 to 100!!')  
    elif(GuessNum in range(number + 1, number + 10)or GuessNum in range(number - 10, number - 1)):
        print('You\'re really close to the number.') # There are eight spaces in front of print.
    elif (GuessNum in range(number + 11, number + 30)or GuessNum in range(number - 30, number - 11)):
        print('You\'re close, but you could do better.')
    elif (GuessNum in range(number + 31, number + 60)or GuessNum in range(number - 60, number - 31)):
        print('Nevermind, your head isn\'t in the game...')
    elif (GuessNum in range(number + 61, number + 999)or GuessNum in range(number - 999, number - 61)):
        print('Stop making fun of the game...')    
    elif GuessNum == number:
#prints message congratulating the user with the number of tries        
        print('Good job, ' + Name + '! You guessed my number in ',TryNum,' tries!!')
        break


