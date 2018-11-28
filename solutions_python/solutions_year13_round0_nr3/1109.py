'''
Created on Apr 13, 2013

@author: kai
'''
from scipy import *
import sys

def isPalindrome(number):
    reverseNumber = str(number)[::-1]

    if number == int(reverseNumber):
        return True
    else:
        return False

if __name__ == '__main__':
    hndlin = open(sys.argv[1],'rt')
    hndlout = open(sys.argv[2],'w')
    
    numberCases = int(hndlin.readline())
    
    for index in range(0,numberCases):

        buttomLimit,upperLimit = hndlin.readline().rstrip('\n').split(' ')
        buttomLimit = int(buttomLimit)
        upperLimit = int(upperLimit)
        
        buttomLimitSquareRoot = int(sqrt(buttomLimit))
        upperLimitSquareRoot = int(sqrt(upperLimit))
        
        fair_and_Square_Found = 0
        
        for number in range(buttomLimitSquareRoot,upperLimitSquareRoot+1):
            if isPalindrome(number):
                candidate = number**2
                if isPalindrome(candidate) and candidate>=buttomLimit:
                    fair_and_Square_Found +=1
                    print number
        
        output = "Case #"+str(index+1)+": "+ str(fair_and_Square_Found) + '\n'

        #print output
        hndlout.write(output)
        
    hndlin.close()
    hndlout.close()