#!/usr/bin/env python3.3
"""
Google Code Jam 2013 Qualification Round
Problem C: Fair and Square

Find square numbers where it and its square root are palindromic

@author Jeffrey Owens
"""

import math

inputFile = 'C-small-attempt1.in'
outputFile = 'C-small.out'

inFile = open(inputFile, 'r')
# Read number of cases from first line
numCases=int(inFile.readline())

outFile = open(outputFile, 'w')

for case in range(1, numCases + 1):

    # Read range line
    bufferLine = inFile.readline()
    # Convert range line to usable ints
    lowerBound, upperBound = map(int, bufferLine.split(' '))

    # Lower the lower bound so that lower square root numbers are checked
    newLowBound = int(math.sqrt(lowerBound))
    
    countPal = 0
    
    # Search square root numbers for square numbers
    # Inclusive of upperBound (just in case function changes later)
    for i in range(newLowBound, upperBound + 1):

        # Calculate square for processing
        square = i**2
        if square > upperBound: # stop if out of bounds
            break

        if square < lowerBound: # skip any lower
            continue

        if str(i) != str(i)[::-1]: # If square root number isn't palindrome
            continue

        if str(square) == str(square)[::-1]: # Square palindrome found
            countPal = countPal + 1
        
        
    stringOut = 'Case #' + str(case) + ': ' + str(countPal)
    print(stringOut)
    outFile.write(stringOut + '\n')

# end for (case)

# Cleanup
inFile.close()
outFile.close()
