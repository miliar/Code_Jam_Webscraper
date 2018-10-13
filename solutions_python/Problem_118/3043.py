#!/bin/python
import math

def perfectSquares(min, max):
    lowest = int(math.ceil(math.sqrt(min)))
    heighest = int(math.sqrt(max))
    return [n**2 for n in range(lowest, heighest + 1)]

def isPalindrome(theWord):
    return (theWord==theWord[::-1])

def printOutput(listOfLists):
    caseNo = 0
    for ar in listOfLists:
        caseNo = caseNo + 1
        if (len(ar) == 2):
            pSquares = perfectSquares(ar[0], ar[1])
            pp = [int(x) for x in pSquares if isPalindrome(str(x))]
            ppp = [int(y) for y in pp if isPalindrome(str(int(math.sqrt(y))))]
            print 'Case #' + `caseNo` + ': ' + `len(ppp)`

size = int(raw_input())
inputList = []
if (size >= 1 and size <= 100):
    caseNo = 0
    while (size > 0):
        size = size - 1
        ar = [int(i) for i in raw_input().strip().split()]
        inputList.append(ar)

    printOutput(inputList)
else:
    exit()


