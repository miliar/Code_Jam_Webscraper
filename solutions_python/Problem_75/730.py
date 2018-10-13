#!/usr/bin/python

import sys

# Read the input file.
f = open(sys.argv[1], "r")
fo = open(sys.argv[1].replace("in", "out"), "w")
lines = f.readlines()
f.close()

testCases = int(lines.pop(0).strip())

class CombinationResult:
    def __init__(self, a, b, result):
        self.a = a
        self.b = b
        self.result = result

i = 0
while i < testCases:
    i += 1

    magic = lines.pop(0).strip().split(" ")

    # Oh, oh, oh... It's magic!
    goodCombinations = int(magic[0])
    badCombinations = int(magic[goodCombinations + 1])
    characters = int(magic[goodCombinations + 1 + badCombinations + 1])
    characterSet = magic[goodCombinations + 1 + badCombinations + 2]
    result = []

    combinations = []

    j = 0
    while j < goodCombinations:
        j += 1

        combinations.append(CombinationResult(magic[j][0], magic[j][1], magic[j][2]))

    j = 0
    while j < badCombinations:
        j += 1

        combinations.append(CombinationResult(magic[goodCombinations + 1 + j][0], magic[goodCombinations + 1 + j][1], None))

    j = 0
    while j < characters:
        result.append(characterSet[j])
        amount = len(result)

        if amount >= 2:
            magicElement = result[amount - 2]
            magicElement2 = result[amount - 1]

            found = False
            replace = None
            for combination in combinations:
                if not found and ((combination.a == magicElement and combination.b == magicElement2) or (combination.a == magicElement2 and combination.b == magicElement)):
                    found = True
                    replace = combination.result

            if not found:
                k = 0
                while k < amount - 1 and not found:
                    magicElement = result[k]
                    magicElement1 = result[k - 1]

                    for combination in combinations:
                        if combination.result == None and found == False and ((combination.a == magicElement and combination.b == magicElement2) or (combination.a == magicElement2 and combination.b == magicElement)):
                            found = True

                    k += 1

            if found:
                if replace != None:
                    result.pop()
                    result.pop()

                    result.append(replace)
                else:
                    result = []

        j += 1

    resultString = "["

    j = 0
    amount = len(result)
    while j < amount:
        resultString += result[j]
        j += 1

        if j != len(result): resultString += ", "


    resultString += "]"

    fo.write("Case #" + str(i) + ": " + resultString + "\n")

fo.close()
