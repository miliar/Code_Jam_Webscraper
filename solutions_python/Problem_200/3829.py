"""
    Calculating tidy numbers
"""

def main():
    fileInput = open("input.txt", 'r')
    intCaseCount = int(fileInput.readline())
    aintCases = [int(strCase) for strCase in fileInput.readlines()]
    fileInput.close()
    fileOutput = open("output.txt", 'w')
    for intCaseIndex in range(intCaseCount):
        fileOutput.write(solveCase(intCaseIndex, aintCases[intCaseIndex]))
    fileOutput.close()
    

def solveCase(intCaseIndex, intNum):
    while not isTidy(intNum):
        intBreakIndex = findBreak(intNum)
        intNum = decreaseOrder(intNum, intBreakIndex)
    return "Case #{0}: {1}\n".format(intCaseIndex + 1, intNum)


def isTidy(intNum):
    strNum = str(intNum)
    intCurrDigit = 0
    intPrevDigit = 0
    for char in strNum:
        intCurrDigit = int(char)
        if intCurrDigit < intPrevDigit:
            return False
        intPrevDigit = intCurrDigit
    return True


def findBreak(intNum):
    strNum = str(intNum)
    intCurrDigit = 0
    intPrevDigit = 0
    for intIndex in range(len(strNum)):
        intCurrDigit = int(strNum[intIndex])
        if intCurrDigit < intPrevDigit:
            return intIndex - 1
        intPrevDigit = intCurrDigit
    return -1
    

def decreaseOrder(intNum, intBreakIndex):
    assert(intBreakIndex >= 0)
    lstNum = strToList(str(intNum))
    lstNum[intBreakIndex] -= 1
    for intIndex in range(intBreakIndex + 1, len(lstNum)):
        lstNum[intIndex] = 9
    if lstNum[0] == 0:
        lstNum = lstNum[1:]
    intNum = int(listToStr(lstNum))
    return intNum
        

def strToList(strString):
    aArray = []
    for char in strString:
        aArray.append(int(char))
    return aArray


def listToStr(aArray):
    strString = ""
    for intDigit in aArray:
        strString += str(intDigit)
    return strString

    
if __name__ == "__main__":
    main()
