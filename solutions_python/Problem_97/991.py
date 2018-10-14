#!/usr/bin/env python2
import sys
import math
import copy
class Test:
    pass
class Result:
    pass


def parseInput(path):
    ret = []
    testFile = open(path)
    inputSize = int(testFile.readline())

    for i in range(inputSize):
        text = testFile.readline().split()
        test = Test()
        test.min = int(text[0])
        test.max = int(text[1])
        ret.append(test)

    return ret

def parseNumber(number):
    ret = []
    base = 10
    remaining = number

    while remaining > 0:
        ret.append(remaining % base)
        remaining /= base

    ret.reverse()
    return ret

def unparseNumber(number):
    ret = 0
    reverseNumber = copy.copy(number)
    reverseNumber.reverse()
    base = 1

    for x in reverseNumber:
        ret += x * base
        base *= 10
    return ret

def countDigits(number):
    remainder = number
    digits = 0

    while remainder > 0:
        remainder /= 10
        digits += 1

    return digits

def rotateNumber(number, digitCount, rotDigits):
    factor = 10 ** rotDigits
    part1 = number % factor
    part2 = number / factor

    return part2 + part1 * 10**(digitCount-rotDigits)

def solve(test):
    recycleCount = 0
    digitCount = countDigits(test.max)
    checked = [False for x in range(test.max-test.min+1)]

    for i in range(test.min, test.max+1):
        if not checked[i-test.min]:
            matches = 1
            for j in range(digitCount-1):
                number = rotateNumber(i, digitCount, j+1)
                if test.max >= number >= test.min:
                    if number != i and not checked[number-test.min]:
                        matches += 1
                    checked[number-test.min] = True
            recycleCount += matches * (matches - 1) / 2

    return recycleCount



tests = parseInput(sys.argv[1])
results = []
for test in tests:
    results.append(solve(test))

for i in range(len(results)):
    print "Case #{0}: {1}".format(i+1, results[i])