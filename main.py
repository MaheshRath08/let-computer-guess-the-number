import random

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

guessIt(100)