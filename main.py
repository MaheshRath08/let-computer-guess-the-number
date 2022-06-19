import random

print("-------Welcome to this game------")
print("----First guess a number between 1 to 1000----")
print("----Run the program and computer will try to guess it----")
print("----if computer's guess is lower, type L----")
print("----if computer's guess is higher, type H----")
print("----if computer's guess is correct, type C----")

def guessIt(x):
    low = 1
    high = x
    feedback =''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low     #Or high since low = high
        feedback = input(f"Is {guess} your number ? 'H' for too high, 'L' for too low, 'c' for correct:").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print("-----------------------------------------------------------------")        
    print(f"YaY!!!! Computer has successfully guessed the number, {guess}.....")
    print("-----------------------------------------------------------------")       

askEm = input("Are you ready? (y/n):\n").lower()
if askEm != "y":
    quit()
else:
    try:
        guessIt(1000)
    except ValueError:
        print("Something went wrong!!!!!")