def doMagic(rowNum1, cardArray1, rowNum2, cardArray2):
    rowNums1 = {cardArray1[x][rowNum1] for x in range(4)}
    rowNums2 = {cardArray2[x][rowNum2] for x in range(4)}
    commonNums = rowNums1 & rowNums2
    print("DBG:")
    print(rowNums1)
    print(rowNums2)
    print(commonNums)
    return commonNums

def readInput():
    testCaseCount = int(input())
    out = "Case #{}: {}"
    for caseNum in range(testCaseCount):
        rowNum1 = int(input())
        cardArray1 = [[] for i in range(4)]
        for _ in range(4):
            for i, num in enumerate(input().split()):
                cardArray1[i].append(int(num))
        rowNum2 = int(input())
        cardArray2 = [[] for i in range(4)]
        for _ in range(4):
            for i, num in enumerate(input().split()):
                cardArray2[i].append(int(num))
        magicResult = doMagic(rowNum1 - 1, cardArray1, rowNum2 - 1, cardArray2)
        if len(magicResult) == 0:
            print(out.format(caseNum + 1, "Volunteer cheated!"))
        elif len(magicResult) > 1:
            print(out.format(caseNum + 1, "Bad magician!"))
        else:
            print(out.format(caseNum + 1, list(magicResult)[0]))

if __name__ == "__main__":
    readInput()
