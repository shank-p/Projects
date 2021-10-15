# Activity to guess a number 

import random

lives = 5
q_order = random.sample(range(5),5)   

print("\n \n =========================================================================================================== \n")

def generate_no():
    n = random.randint(1,101)
    print(" A number from 1 to 100 has been generated . Start Guessing :) ")
    return(n)
key = generate_no()

def add_digits():
    sum = 0
    for digits in str(key):
        sum += int(digits)
    return (sum)

def check_prime():
    for i in range(3,key):
        if ((key%i) == 0):
            return(False)
        else:
            return(True)

def clue():
    for i in q_order:
        if (i == 0):
            if( key%2 == 0):
                print("Number is even.")
            else:
                print("Number is odd.")
        elif (i == 1):
            if (key >= 50):
                print("The number is greater than or equal to 50.")
            else:
                print("The number is lesser than or equal to 50.")
        elif (i == 2):
            if (key%10 == 0):
                print("The Number is multiple of 10.")
            else:
                print("The number is not a multiple of 10.")
        elif(i==3):
            new_key = add_digits()
            if (new_key > 9):
                print("Adding the digits of the number gives a two digit number.")
            else:
                print("Adding the digits of the number gives a single digit number.")
        elif(i==4):
            x = check_prime()
            if(x):
                print("Number is Prime .")
            else:
                print("Number is not Prime.")
        q_order.pop(0)
        break

def inp():
    try:
        user_input = int(input(" Enter your guess : "))
        return user_input
    except:
        print("Enter valid input.")
        inp()

while(lives):
    clue()
    guess = inp()
    if (guess == key):
        print(" \n U Won !!!")
        guess = True
        break
    else:
        lives = lives - 1
        print(" Check Lives :",lives)

if(guess != True):
    print(" \n U Lost :( , Better luck next time ")
    print(" The number was ",key)







