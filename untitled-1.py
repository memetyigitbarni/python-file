import random

def main():
    randnum = random.randint(1,10)
    tries=5
    while(tries>0):
        guess = int(input("Gueass a number between 1 and 10 "))
        if (guess == randnum):
            print("You Win")
            break
        else:
            print("Try Again")  
            tries = tries - 1
            print("You have " + str(tries) + " tries left")
        if(tries==0):
            print("You Lose")
if __name__ == "__main__":
        main() 
        
    