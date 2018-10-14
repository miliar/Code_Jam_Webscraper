debug = False
searchPhrase = "welcome to code jam"
maxDepth = -1
cache = dict()

def main(inputFilename):
    f = open(inputFilename)
    testCases = getArgs(f)
    if debug:
        printArgs(testCases)
    solveTestCases(testCases)

def getArgs(f):
    testCases = []
    N = int(f.readline())
    for i in range(N):
        text = readlineWithoutNewline(f)
        testCase = TestCase(text)
        testCases.append(testCase)
    return testCases

def readlineWithoutNewline(f):
    line = f.readline()
    if line[-1:] == "\n":
        line = line[:-1]
    return line

def printArgs(testCases):
    print("N (number of test cases): {0}".format(len(testCases)))
    print()
    for testCase in testCases:
        print(testCase.text)
    print()

def solveTestCases(testCases):
    for testCase in testCases:
        solveTestCase(testCase)
    printSolutions(testCases)

def solveTestCase(testCase):
    testCase.numAppearances = getNumAppearances(testCase.text, searchPhrase)

def getNumAppearances(haystack, needle):
    return getNumAppearancesRecursive(haystack, needle)

def getNumAppearancesRecursive(haystack, needle):
    key = (haystack, needle)
    if key in cache:
        return cache[key]
    else:
        if needle == "":
            num = 1    
        elif len(needle) > len(haystack):
            num = 0
        else:
            firstLetterIndex = haystack.find(needle[0])
            if firstLetterIndex < 0:
                num = 0
            else:
                newHaystack = haystack[firstLetterIndex + 1:]
                consumingNum = getNumAppearancesRecursive(newHaystack, needle[1:])
                nonConsumingNum = getNumAppearancesRecursive(newHaystack, needle)
                num = consumingNum + nonConsumingNum
        cache[key] = num
        return num

def printSolutions(testCases):
    for (testCaseNumber, testCase) in enumerate(testCases):
        fourDigitNumAppearances = getSetWidthNumber(testCase.numAppearances, 4)
        print("Case #{0}: {1}".format(1 + testCaseNumber, fourDigitNumAppearances))
        
def getSetWidthNumber(num, numDigits):
    atLeastWidthNumber = num % pow(10, numDigits)
    return "%0{0}d".format(numDigits) % atLeastWidthNumber

class TestCase:
    def __init__(self, text):
        self.text = text
        self.numAppearances = 0

if (__name__ == "__main__"):
    import sys
    inputFilename = sys.argv[1]
    main(inputFilename)
