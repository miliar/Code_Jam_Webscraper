#Tidy Numbers
from sys import *

def isTidy(num): #Argument in string format for easy iteration
    #Checks if the number is tidy (digits are in ascending order)
    #Returns a boolean
    Tidyness = False    #Initialise the return value to False as default
    c = 1               #Initialise counter for loop
    while c < len(num): #Iterates through each character in the num string
        if int(num[c]) < int(num[c-1]): #If the number doesn't satisfy the criteria, 
            break                       #end the loop and skip the else statement following it.
        else:                           
            c += 1  #Increment to keep iterating and not get into an infinite loop
    else:               #Only executes if the loop ended normally (when condition is false)
        Tidyness = True #Updates the boolean to True because the number satisfies the criteria
    return Tidyness

def main(num):
    lastTidyNum = int(num)
    while not isTidy(str(lastTidyNum)):
        lastTidyNum -= 1
    return lastTidyNum

cases = []
for i in range(0,int(stdin.readline())):
    cases.append(stdin.readline().rstrip())
    #print cases #For debug

for i in cases:
    print "Case #" + str(cases.index(i) + 1)+":", main(i)
