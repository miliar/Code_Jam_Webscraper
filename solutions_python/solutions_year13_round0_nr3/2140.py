'''
Created on Apr 12, 2013
Google Code Jam Qualification Round 2013
Problem A

@author: Jared Feldman
'''

import math

def isSquare(x):
    if (math.sqrt(x) % 1) == 0:
        return True
    else:
        return False

def isPalindrome(x):
    length = len(str(x))
    
    if length == 1:
        return True
    
    x = str(x)
    
    if (length % 2) == 1:
        middleIndex = length/2
        x = x[0:middleIndex] + x[middleIndex+1:length]
        length -= 1
        
    i = 0
    while i <= length/2:
        if x[i] != x[length-1-i]:
            return False
        i += 1
        
    return True
    
def isValid(x):
    
    
    if isPalindrome(x) and isSquare(x):
        if isPalindrome(int(math.sqrt(x))):
            return True
        
    return False

def getResult(lower, upper):
    index = lower
    count = 0
    
    while (index <= upper):
        if isValid(index):
            count += 1
        index += 1
            
    return count

if __name__ == '__main__':
    # I/O Files
    readFile = open("C-small-attempt0.in.txt","r+")
    writeFile = open("C-small-attempt0.out.txt","w+")
    
    numberOfCases = int(readFile.readline())
    currentCase = 0    
        
    # Loop through all cases
    while (currentCase < numberOfCases):
        
        # Increment case number
        currentCase += 1
        
        # Read the 4x4 grid
        bounds = str.split(str.strip(readFile.readline())," ")
        
        lower = int(bounds[0])
        upper = int(bounds[1])
        
        print "Case #%s: %s" %(currentCase, getResult(lower, upper))
        writeFile.write("Case #%s: %s\n" %(currentCase, getResult(lower, upper)))