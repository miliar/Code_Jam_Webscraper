#!/usr/bin/python

import itertools
import sys

# Read the input file.
f = open(sys.argv[1], "r")
fo = open(sys.argv[1].replace("in", "out"), "w")
lines = f.readlines()
f.close()

testCases = int(lines.pop(0).strip())

def dec2bin(n):
    bStr = ""
    if n == 0: return "0"
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

# Do not use the following function in production code, ...
# ..., unless your name is Patrick and you like counting candies.
def badBinaryComputation(a, b):
    # Strip extra zeros.
    while len(a) > 0 and a[0] == "0":
        a = a[1:]

    while len(b) > 0 and b[0] == "0":
        b = b[1:]

    # Add extra zeros.
    diff = abs(len(a) - len(b))

    if len(a) < len(b):
        a = diff * "0" + a
    elif len(a) > len(b):
        b = diff * "0" + b

    result = ""
    i = 0
    while i < len(a):
        temp = "0"

        if a[i] == "1" and b[i] == "0":
            temp = "1"
        if a[i] == "0" and b[i] == "1":
            temp = "1"

        result += temp

        i += 1

    return result

i = 0
while i < testCases:
    print i
    i += 1

    amount = int(lines.pop(0).strip())
    candies = lines.pop(0).strip().split(" ")

    while len(candies) > amount:
        candies.pop()

    highestFound = -1

    split = 0
    while split < amount:
        split += 1

        seanCombo = itertools.combinations(candies, split)

        for sean in seanCombo:
            patrick = []

            for candy in candies:
                patrick.append(candy)

            validSumSean = 0
            sumSean = ""
            for candy in sean:
                validSumSean += int(candy)
                binCandy = dec2bin(int(candy))
                sumSean = badBinaryComputation(sumSean, binCandy)

                if candy in patrick:
                    patrick.remove(candy)

            sumPatrick = ""
            for candy in patrick:
                binCandy = dec2bin(int(candy))

                sumPatrick = badBinaryComputation(sumPatrick, binCandy)

            intSumSean = 0
            if sumSean != "" and sumPatrick != "":
                intSumSean = int(sumSean, 2)
                intSumPatrick = int(sumPatrick, 2)

                if intSumSean == intSumPatrick and highestFound < validSumSean:
                    highestFound = validSumSean

    if highestFound == -1:
        fo.write("Case #" + str(i) + ": NO\n")
    else:
        fo.write("Case #" + str(i) + ": " + str(highestFound) + "\n")

fo.close()
