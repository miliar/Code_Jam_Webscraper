#!/usr/bin/env python
__author__ = 'pal-andreich'


class TestCase:
    def __init__(self, numCases):
        self.numCases = numCases
        self.cases = {}
        self.__currentCase = 0

    def addTestCase(self, **kwargs):
        self.cases[self.__currentCase] = kwargs
        self.__currentCase += 1


def getTestCases(fileName):
    with open(fileName) as inputFile:
        content = inputFile.read()
        lines = content.split('\n')
        lineNum = 0
        testCase = None
        for line in lines:
            if lineNum == 0:
                testCase = TestCase(int(line))
                lineNum += 1
            else:
                if line:
                    params = line.split()
                    testCase.addTestCase(
                        numOfGooglers=int(params[0]),
                        numOfSupriseTriples = int(params[1]),
                        leastResult = int(params[2]),
                        overalls = [int(overall) for overall in params[3:]]
                    )
    return testCase


def getSurpriseMaxMark(overall):
    marks = range(11)
    results = []
    for x in marks:
        for y in marks:
            for z in marks:
                if(
                    (x + y + z == overall) and
                    max(abs(x - y), abs(y - z), abs(z-x)) == 2
                    ):
                    results.append(max(x, y, z))
    if results:
        return max(results)


def getMaxMark(overall):
    marks = range(11)
    results = []
    for x in marks:
        for y in marks:
            for z in marks:
                if(
                    (x + y + z == overall) and
                    max(abs(x - y), abs(y - z), abs(z-x)) < 2
                ):
                    results.append(max(x, y, z))
    if results:
        return max(results)

def main():
    inputFile = 'data/B-large.in'
    outputFile = 'data/b_output.out'
    caseResponseTemplate = 'Case #{0}: {1}\n'

    testCases = getTestCases(inputFile)

    with open(outputFile, 'w') as outFile:
        for numCase, case in testCases.cases.iteritems():
            overalls = sorted(case['overalls'], reverse=True)
            for overall in overalls:
                if getMaxMark(overall) < case['leastResult']:
                    if case['numOfSupriseTriples']:
                        if getSurpriseMaxMark(overall) < case['leastResult']:
                            case['numOfGooglers'] -= 1
                        else:
                            case['numOfSupriseTriples'] -= 1
                    else:
                        case['numOfGooglers'] -= 1
            outFile.write(caseResponseTemplate.format(numCase + 1, case['numOfGooglers']))


if __name__ == '__main__':
    main()