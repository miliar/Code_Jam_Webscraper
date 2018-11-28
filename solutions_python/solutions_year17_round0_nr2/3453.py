
def generateDigits(number):
    return [int(x) for x in str(number)]

def isTinyNumber(digits):
    temp = digits[:]
    return temp == sorted(temp)

def lastTinyNumber(digits):
    if isTinyNumber(digits):
        return int("".join([str(x) for x in digits]))

    for length in range(len(digits), 0, -1):
        if isTinyNumber(digits[0:length]):
            tinyPart = int("".join([str(x) for x in digits[0:length]]))
            if isTinyNumber(generateDigits(tinyPart - 1)):
                if tinyPart - 1 > 0:
                    return int(str(tinyPart - 1) + "9" * (len(digits) - length))
                else:
                    return int("9" * (len(digits) - length))

class TestCase:
    def __init__(self, caseIndex):
        self.caseIndex = caseIndex

    def parseInput(self):
        self.N = raw_input()
        self.N = int(self.N)

        self.lastTinyNumber = 0

    def run(self):
        self.lastTinyNumber = lastTinyNumber(generateDigits(self.N))

    def generateOutput(self):
        print "Case #%d: %d" % (self.caseIndex, self.lastTinyNumber)

for caseIndex in range(1, int(raw_input()) + 1):
    testCase = TestCase(caseIndex)
    testCase.parseInput()
    testCase.run()
    testCase.generateOutput()
