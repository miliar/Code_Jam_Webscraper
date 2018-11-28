#!/usr/bin/python
import sys
import math

# taken from http://stackoverflow.com/questions/199184/how-do-i-check-if-a-number-is-a-palindrome
def isPalindrome(number):
    n = number
    rev = 0
    while (number > 0):
        dig = number % 10
        rev = rev * 10 + dig
        number = number / 10
    if n == rev:
        return True
    return False

# taken from http://stackoverflow.com/questions/15390807/integer-square-root-in-python
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def solveCase(rangeMin, rangeMax):
    found = 0
    for numberTest in xrange(rangeMin, rangeMax+1):
        if isPalindrome(numberTest):
            sqrtNum = isqrt(numberTest)
            # ensure it is an accurate square root
            if sqrtNum * sqrtNum == numberTest:
                if isPalindrome(sqrtNum):
                    found += 1
    return str(found)

inputFile = open(sys.argv[1], 'r')

outputFile = open(sys.argv[2], 'w')
outputString = ""

caseAmount = int(inputFile.readline())

lines=inputFile.readlines()

#print caseAmount

currentLine = 0

for case in range(0,caseAmount):
    range = lines[currentLine].split()

    currentLine += 1

    result = solveCase( int(range[0]), int(range[1]) )
    print "Case #" + str(case+1) + ": " + result
    outputString = outputString + "Case #" + str(case+1) + ": " + result + "\n"

outputFile.write(outputString)


    
    