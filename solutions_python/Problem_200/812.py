#!/usr/bin/env python3

import sys

def decrementDigit(d):
    if d == '0':
        d = '9'
    n = int(d)
    return str(n-1)

def solveCase(number):
    newNumber = list(reversed(number))
    lastDigit = newNumber[0]
    for i in range(0, len(newNumber)):
        d = newNumber[i]
        if d > lastDigit:
            newNumber[i] = decrementDigit(d)
            for j in range(0, i):
                newNumber[j] = '9'
        lastDigit = newNumber[i]
    answer = ''.join(reversed(newNumber)).lstrip('0')
    assert(checkNumber(answer))
    return answer

def checkAnswer(number, answer):
    for n in range(int(answer)+1, int(number)+1):
        if checkNumber(str(n)):
            return False
    return checkNumber(answer)

def checkNumber(number):
    largestSoFar = '0'
    for d in number:
        if largestSoFar > d:
            return False
        if largestSoFar < d:
            largestSoFar = d
    return True

def runCases():
    next(sys.stdin)
    for i, line in enumerate(sys.stdin):
        answer = solveCase(line.strip());
        print('Case #{}: {}'.format(i+1, answer))

if __name__ == '__main__':
    runCases()

