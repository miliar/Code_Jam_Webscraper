import sys
import math

counterList = list()
boundList = list()

def getSplitedList(s):
    s = s.strip('\n')
    sList = s.split(" ")
    return [int(i) for i in sList]

def readFile():
    f = open(sys.argv[1])
    caseNum = int(f.readline().strip('\n'))
    for i in range(caseNum):
        boundList.append(getSplitedList(f.readline()))
    f.close()

def isSquare(num):
    sq = math.sqrt(num)
    return int(sq) == sq

def isPalindrome(num):
    isPa = True
    numStr = str(num)
    numlen = len(numStr)
    checkBound = numlen / 2
    for i in range(0, checkBound):
        if numStr[i] != numStr[numlen-1-i]:
            isPa = False
    return isPa

def isFair(num):
    isS = isSquare(num)
    isP = isPalindrome(num)
    isPS = isPalindrome(int(math.sqrt(num)))
    return isS and isP and isPS

def process():
    for boundPair in boundList:
        low = boundPair[0]
        high = boundPair[1]
        counter = 0
        for num in range(low, high + 1):
            if isFair(num):
                counter += 1
        counterList.append(counter)

def result():
    caseIndex = 1
    f = open('result.out', 'w')
    for count in counterList:
        resultStr = "Case #%d: %d\n" % (caseIndex, count)
        f.write(resultStr)
        caseIndex += 1
    f.close()

def main():
    readFile()
    process()
    result()

main()
