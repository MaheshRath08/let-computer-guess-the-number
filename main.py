import random
#Guide the user
print("-------Welcome to this game------")
print("----First choose a number between 1 to 1000 in your brain----")
print("----Run the program and computer will try to guess it----")
print("----if computer's guess is lower, type L----")
print("----if computer's guess is higher, type H----")
print("----if computer's guess is correct, type C----")
#define the function
def guessIt(x):      
    low = 1
    high = x
    feedback =''         
    while feedback != "c":     #iterate until it's correct
        if low != high:         #incase it comes to that 
            guess = random.randint(low, high)    #regular guess
        else:
            guess = low     #Or high since low = high
        feedback = input(f"Is {guess} your number ? 'H' for too high, 'L' for too low, 'c' for correct:").lower()     #asks for feedback and takes 3 input
        if feedback == 'h':
            high = guess - 1      #cancels out the numbers higher than the previous guess
        elif feedback == 'l':
            low = guess + 1        #cancels out the numbers lower than the previous guess
    print("-----------------------------------------------------------------")        
    print(f"YaY!!!! Computer has successfully guessed the number, {guess}.....")
    print("-----------------------------------------------------------------")       

askEm = input("Are you ready? (y/n):\n").lower()      #pre-program message to the user
if askEm != "y":
    quit()
else:
    try:
        guessIt(1000)                             #finally call the function 
    except ValueError:                            #incase user types wrong values and value error pops-up
        print("Something went wrong!!!!!")        #or if user gets trapped with their feedbacks