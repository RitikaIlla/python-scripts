# python2.7
import random
n = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while n != "guess":
    if guess < n:
        print "Your guess is low"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print "Your guess is high"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "You guessed it correctly!"
        break
    print