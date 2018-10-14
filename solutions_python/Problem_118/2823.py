import math

def getStartSqrt(num):
    retVal = pow(num,0.5)
    return math.ceil(retVal)

def getEndSqrt(num):
    retVal = pow(num,0.5)
    return math.floor(retVal)

def isPalin(num):
    num1 = num
    arr = []
    while num1 != 0 :
        arr.append(num1 % 10)
        num1 = num1 / 10
    arr1 = arr[:]
    arr1.reverse()
    retVal = True
    for i in range(len(arr)):
        if arr[i] != arr1[i]:
            retVal = False
            break
    return retVal

WORDLIST_INFILENAME = "C-small-attempt0.in"
inFile = open(WORDLIST_INFILENAME, 'r', 0)
WORDLIST_OUTFILENAME = "output.in"
outFile = open(WORDLIST_OUTFILENAME, 'w', 0)
noOfTestCases = inFile.readline()
for iTestCase in range(int(noOfTestCases)):
    line = inFile.readline()
    char = line.split()
    startSqr = int(char[0])
    EndSqr = int(char[1])
    start = int(getStartSqrt(startSqr))
    end = int(getEndSqrt(EndSqr))
    arrNum = []
    check = True
    index = start
    while True:
        if index > end:
            break
        if isPalin(index):
            arrNum.append(index)
        index = index + 1

    arrFairSqr = []
    for num in arrNum:
        sqr = num * num
        if isPalin(sqr):
            arrFairSqr.append(num)

    outFile.writelines("Case #"+str(iTestCase+1)+": "+str(len(arrFairSqr))+"\n")
inFile.close()
outFile.close()

