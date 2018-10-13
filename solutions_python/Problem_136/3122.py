#
# Google Code Jam 2014
# 
# Author: Tim van Deurzen <tim.vandeurzen@gmail.com>
#

import sys

def parseInput(fileName):
    """
    Parse the input according to the format described on the code jam webpage.
    """

    with open(fileName) as fp:
        dataRead = fp.readlines()

    data = [x.strip() for x in dataRead]

    numberOfCases = int(data[0])
    parsedInput = []
    caseIndex = 1
    for line in data[1:]:
        parsedLine = parseLine(line);
        parsedInput.append({ 'caseIndex': caseIndex
                           , 'C': parsedLine[0]
                           , 'F': parsedLine[1]
                           , 'X': parsedLine[2]
                           })
        caseIndex += 1

    if len(parsedInput) == numberOfCases:
        return parsedInput
    else:
        raise "Error parsing input."

def parseLine(line):
    """
    Parse a single line of input
    """
    return list(map(float, line.split()))

def runTestCase(testCase):
    """
    Run a single test case.
    """
    cookiesPerSecond = 2.0

    result = 0
    if testCase['X'] <= testCase['C']:
        result = testCase['X'] / cookiesPerSecond
    else:
        # Find the point at which it becomes better to NOT buy a factory.
        timeForFactory = testCase['C'] / cookiesPerSecond
        nextTimeWithoutFactory = testCase['X'] / (cookiesPerSecond + testCase['F'])
        timeWithFactory = timeForFactory + nextTimeWithoutFactory
        timeWithoutFactory = testCase['X'] / cookiesPerSecond

        while timeWithFactory < timeWithoutFactory:
            result += timeForFactory
            cookiesPerSecond += testCase['F']
            timeForFactory = testCase['C'] / cookiesPerSecond
            nextTimeWithoutFactory = testCase['X'] / (cookiesPerSecond + testCase['F'])
            timeWithFactory = timeForFactory + nextTimeWithoutFactory
            timeWithoutFactory = testCase['X'] / cookiesPerSecond

        result += timeWithoutFactory
        
    print("Case #{}: {:.7f}".format(testCase['caseIndex'], result))


def main():
    if len(sys.argv) < 2:
        print("Usage: python {} <file>\n".format(sys.argv[0]))
        sys.exit(0)
    else:
        for case in parseInput(sys.argv[1]):
            runTestCase(case)

main()
