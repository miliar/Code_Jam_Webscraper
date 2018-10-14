debug = False

def main(inputFilename):
    f = open(inputFilename)
    (L, D, N, words, testCases) = getArgs(f)
    if debug:
        printArgs(L, D, N, words, testCases)
    solveTestCases(words, testCases)        

def getArgs(f):
    (Lstr, Dstr, Nstr) = f.readline().split()
    L = int(Lstr)
    D = int(Dstr)
    N = int(Nstr)
    
    words = []
    for i in range(D):
        word = f.readline()[:-1]
        words.append(word)

    testCases = []
    for i in range(N):
        testCase = TestCase(f.readline()[:-1])
        testCases.append(testCase)

    return (L, D, N, words, testCases)

def printArgs(L, D, N, words, testCases):
    print("L (letters per word): " + str(L))
    print("D (number of words):" + str(D))
    print("N (number of test cases):" + str(N))
    print("Words: " + str(words))
    print("Test cases: " + str(testCases))
    print

def solveTestCases(words, testCases):
    prefixesDict = getPrefixesDict(words)
    for (testCaseNumber, testCase) in enumerate(testCases):
        numPossibleWords = getNumPossibleWords(testCase.tokensStr, prefixesDict)
        print("Case #{0}: {1}".format(1+testCaseNumber, numPossibleWords))

def getPrefixesDict(words):
    prefixes = []
    for word in words:
        for length in range(1, 1+len(word)):
            prefixes.append(word[:length])
    return dict.fromkeys(prefixes)

def getNumPossibleWords(tokensStr, prefixesDict):
    return getNumPossibleWordsRecursive("", tokensStr, prefixesDict)
    
def getNumPossibleWordsRecursive(prefix, tokensStr, prefixesDict):
    #print("prefix:{0}, tokensStr:{1}".format(prefix, tokensStr))
    if tokensStr == "":
        return 1
    else:
        numPossibleWords = 0
        (token, restOfTokensStr) = getNextToken(tokensStr)
        for possibility in token:
            newPrefix = prefix + possibility
            if prefixesDict.has_key(newPrefix):
                numPossibleWords += getNumPossibleWordsRecursive(newPrefix, restOfTokensStr, prefixesDict)
        return numPossibleWords

def getNextToken(tokensStr):
    firstChar = tokensStr[:1]
    if firstChar == "(":
        endIndex = tokensStr.index(")")
        possiblitesStr = tokensStr[1:endIndex]
        return (possiblitesStr, tokensStr[endIndex+1:])
    else:
        return (firstChar, tokensStr[1:])

class TestCase:
    def __init__(self, tokensStr):
        self.tokensStr = tokensStr;

    def __repr__(self):
        return str(self.tokensStr)

if (__name__ == "__main__"):
    import sys
    inputFilename = sys.argv[1]
    main(inputFilename)
