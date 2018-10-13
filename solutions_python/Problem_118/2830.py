import sys
import math

f = open("test.in")

numberOfTestCase = f.readline()

for testCase in xrange(int(numberOfTestCase)):
    answerCounter = 0
    line = f.readline().split(" ")
    start = int(line[0])
    end = int(line[1])

    for i in xrange(start, end+1):
        integerStringList = list(str(i))
        integerStringListR = list(str(i))

        integerStringListR.reverse()

        # next integer if not palindrome
        if integerStringList != integerStringListR:
            continue

        # ready to check square
        originalInteger = int(math.sqrt(i))
        squareRootNumber = int(math.sqrt(i) + 0.9)

        originalIntegerList = list(str(originalInteger))
        squareRootNumberList = list(str(squareRootNumber))
        squareRootNumberList.reverse()

        # check is it a square of a paralindrom
        if originalInteger == squareRootNumber and originalIntegerList == squareRootNumberList:
            answerCounter += 1

    sys.stdout.write("Case #")
    sys.stdout.write(str(testCase+1))
    sys.stdout.write(": ")
    sys.stdout.write(str(answerCounter))
    print

