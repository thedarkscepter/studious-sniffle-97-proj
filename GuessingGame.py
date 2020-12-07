import random
n = random.randint(1,10)
chances = 0
print("Guess a number between 1-10")
while chances<5:
    guess = int(input("Enter you Guess"))
    if guess == n:
        print("Congrats :)!! You are one of the few legends")
    elif guess < n:
        print("Your guess was too low :(!! Guess a higher number", guess)
    else:
        print("Your guess was too high :(!! Guess a lower number", guess)
    chances+1
if not chances<5:
    print("YOU LOST!! LOSER", n)