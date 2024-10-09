import random
number = random.randint (1,10)
attempts = 3
count = 1
while count <= attempts:
    guess = int(input("Guess a number 1-10!: "))
    if guess > number:
        print ("Your guess is too high :-(")
    elif guess < number:
        print ("Your guess is too low :-(")
    else:
        print ("Correct")
        break

    count+=1
