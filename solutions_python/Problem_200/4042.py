from sys import argv

def tidyNumBasic(n):
    if (n <= 9):
        return n
    curNum = n
    while (curNum >= 1):
        curNumList = [int(digit) for digit in str(curNum)]
        if (sorted(curNumList) == curNumList):
            return curNum
        curNum -= 1

def tidyNum(n):
    if (n <= 9):
        return n
    found = False
    curNum = n
    while (not found):
        curNumList = [int(digit) for digit in str(curNum)]
        if (curNumList[0]==0):
            del curNumList[0]
        if (sorted(curNumList) == curNumList):
            return curNum
            found = True
        else:
            last = curNumList[0]
            wrongDigitIndex = 0
            for i, digit in enumerate(curNumList):
                if (digit < last):
                    wrongDigitIndex = i
                    break
                else:
                    last = digit
            curNumList[wrongDigitIndex] = 9
            curNumList[wrongDigitIndex - 1] -= 1
            if (wrongDigitIndex < (len(curNumList) - 1)):
                for ind in range(wrongDigitIndex, len(curNumList)):
                    curNumList[ind] = 9
            curNum = 0
            for i, digit in enumerate(curNumList):
                curNum += digit * (10 ** (len(curNumList) - i - 1))

filename = argv[1]

with open(filename) as f:
    inputData = f.readlines()

inputData = [line.strip() for line in inputData]
inputData = [int(line) for line in inputData]

numInputs = inputData[0]
caseData = inputData[1:]

cases = range(1, numInputs + 1)
with open('output.txt', 'a') as outputFile:
    for i,case in enumerate(cases):
        outStr = "Case #" + str(case) + ": " + str(tidyNum(caseData[i])) + "\n"
        outputFile.write(outStr)
