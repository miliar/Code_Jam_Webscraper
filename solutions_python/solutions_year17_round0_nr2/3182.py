import sys
import os
import re
sys.setrecursionlimit(50000)

def findTidy(num, numberLength):       
    hasDecrease = 0    
    for i in range(1, numberLength):
        currentDigit = num[i]
        previousDigit = num[i-1]
        if(hasDecrease == 1):
            num[i] = 9
            
        if(currentDigit < previousDigit and hasDecrease == 0):
            hasDecrease = 1
            num[i - 1] -= 1
            num[i] = 9
            
        if(i == numberLength - 1 and hasDecrease == 1):
            findTidy(num, numberLength)
         
        if(i == numberLength - 1 and hasDecrease == 0):    
            printString = ''.join(str(e) for e in num)
            printString = printString.lstrip('0')
            print(printString)
            return

#define a function to verify test string
def getTidy(string):
    lineString = re.split('\s+', string)
    num = int(lineString[0])
    num = convert(num)
    
    
    
    
    # iterate though the number array and compare the current num with previous num, start from the second number
    numberLength = len(num)
    # if the number is single digit, return current number
    if numberLength == 1:
        print(num[0])
        return
    findTidy(num, numberLength)
      

    
# convert string to an array of numbers 
def convert(int):
    j = len('{}'.format(int))
    b = [0 for i in range(j)]
    c = 0
    while j > 0:
        b [c] = int % 10**j // 10**(j-1)
        j = j-1
        c = c + 1
        
    return b
        
def main():
    # open and read input file
    content = []
    with open("input.txt") as f:
        content = f.read().splitlines()

        # get first line number as number of iterations
        iterateNum = int(content[0])

    # get each line of test string
    i = 1
    for lineString in range(1, iterateNum + 1):
        print("Case #" + str(i) + ": ", end = "")
        i += 1
        getTidy(string = content[lineString])

        # clode input file
        f.close()
  
  
# calling main function  
main()