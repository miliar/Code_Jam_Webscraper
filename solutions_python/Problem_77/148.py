"""
    Code Jam 2011 Qualification Round, Problem D

    gaz@bitplane.net

"""

import math

with open('input.txt') as inputFile:
    testCount = int(inputFile.readline())
    
    for testNumber in range(testCount):

        # ignore, this isn't c!
        inputFile.readline()

        # read the numbers, but let's zero index them
        allNumbers  = [int(i)-1 for i in inputFile.readline()[:-1].split(' ')]
        sortedCount = sum([1 if i==allNumbers[i] else 0 for i in range(len(allNumbers))])

        attemptCount = len(allNumbers)-sortedCount

        result = str(attemptCount)

        # output the result
        print("Case #{case}: {result}".format(case=testNumber+1, result=result))
