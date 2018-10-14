#!/usr/bin/python

import sys

def Dec2Bin(num):
    binaryNum = ''
    if 0 == num: return '0'
    while num > 0:
        binaryNum += str(num % 2)
        num = num >> 1
    return binaryNum

def main():
    numOfCases = input()
    for currentCase in range(1, numOfCases + 1):
        ''' We input the whole line and split it to
            separate it in to:
            1. The number of snappers
            2. The number of clicks '''
        userInput = raw_input().split()
        numOfSnappers = int(userInput[0])
        numOfClicks = int(userInput[1])

        ''' If we repesent each snapper as a bit, when
            1 = ON
            0 = OFF
            then the "light" will be on if all bits are 1'''

        # Convert number of clicks to binary
        binaryNum = Dec2Bin(numOfClicks)
        
        # If one of the bits turnes out - 0, print OFF
        resultStr = 'ON'
        if len(binaryNum) < numOfSnappers: resultStr = 'OFF'
        else:
            for i in range(numOfSnappers):
                if '0' == binaryNum[i]: resultStr = 'OFF'
        print 'Case #%d: %s' % (currentCase, resultStr)
        
        


if __name__ == '__main__':
    main()
