import random

def main():
    randnum = random.randint(1,10)
    tries=5
    while(tries>0):
        guess = int(input("Guess your number for money: "))
        if (guess == randnum):
            print("You get the money!")
        else:
            print("You don't get the money!  Try again!")
            tries = tries - 1
            print("You have " + str(tries) + " tries left! Or else you will lose the money!")
            
    if(tries==0):
        print("You lose the money!  The number was " + str(randnum) + "!")
if __name__ == "__main__":
    main()
    