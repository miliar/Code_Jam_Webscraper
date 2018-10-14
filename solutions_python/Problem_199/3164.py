
import random

def flip(S, index, size):
    splits = list(S)
    for index in range(index, index + size):
        if splits[index] == "+":
            splits[index] = "-"
        else:
            splits[index] = "+"
    return "".join(splits)

def recursive(S, size, indexes, usedIndexes, counter):
    if S.find("-") == -1:
        return counter
    bestReturnValue = -1
    for index in indexes:
        if index in usedIndexes:
            continue
        if len(usedIndexes) > 0 and index < max(usedIndexes):
            continue
        S = flip(S, index, size)
        usedIndexes.append(index)
        returnValue = recursive(S, size, indexes, usedIndexes, counter + 1)
        if returnValue > bestReturnValue:
            bestReturnValue = returnValue
            #return returnValue
        S = flip(S, index, size)
        usedIndexes.remove(index)
    return bestReturnValue

class TestCase:
    def __init__(self, caseIndex):
        self.caseIndex = caseIndex

    def parseInput(self):
        self.S, self.K = raw_input().split()
        self.K = int(self.K)

        self.result = "IMPOSSIBLE"

    def run(self):
        counter = recursive(self.S, self.K, range(0, len(self.S) - self.K + 1), [], 0)
        if counter > -1:
            self.result = str(counter)

    def generateOutput(self):
        print "Case #%d: %s" % (self.caseIndex, self.result)


for caseIndex in range(1, int(raw_input()) + 1):
    testCase = TestCase(caseIndex)
    testCase.parseInput()
    testCase.run()
    testCase.generateOutput()

