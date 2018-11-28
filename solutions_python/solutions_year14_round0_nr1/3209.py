#
# Google Code Jam 2014
#
# Author: Tim van Deurzen <tim.vandeurzen@gmail.com>
#

import sys

def parseInput(fileName):
    """
    Parse the input following the format described on the code jam web page.
    """
    with open(fileName, 'r') as fp:
        dataRead = fp.readlines()

    data = [x.strip() for x in dataRead]

    parsedInput = []
    numberOfCases = int(data[0])
    offset = 1;
    for caseIndex in range(1, numberOfCases + 1):
        parsedInput.append({ 'caseIndex': caseIndex
                           , 'firstAnswer': int(data[0 + offset])
                           , 'firstShuffle': parseDeck(data[1 + offset:5 + offset])
                           , 'secondAnswer': int(data[5 + offset])
                           , 'secondShuffle': parseDeck(data[6 + offset:10 + offset])
                           })
        offset += 10

    return parsedInput

def parseDeck(cards):
    return [list(map(int, row.split())) for row in cards]

def runTestCase(testCase):
    """
    Run a single test case and output the result.
    """

    firstRow = set(testCase['firstShuffle'][testCase['firstAnswer'] - 1])
    secondRow = set(testCase['secondShuffle'][testCase['secondAnswer'] - 1])

    result = firstRow & secondRow

    if len(result) == 1:
        print("Case #{}: {}".format(testCase['caseIndex'], result.pop()))
    elif len(result) > 1:
        print("Case #{}: Bad magician!".format(testCase['caseIndex']))
    elif len(result) == 0:
        print("case #{}: Volunteer cheated!".format(testCase['caseIndex']))


def main():
    if len(sys.argv) < 2:
        print("Usage: python {} <file>\n".format(sys.argv[0]))
        sys.exit(0)
    else:
        for case in parseInput(sys.argv[1]):
            runTestCase(case)

main()
