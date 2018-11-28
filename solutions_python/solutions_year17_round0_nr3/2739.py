# imports
import math

# filenames
filein = "C-small-1-attempt0.in.txt"
fileout = "C.small-1.answers"

# functions
def findGap(occupiedList):
    x1, x2 = occupiedList[0], occupiedList[1]
    maxGap = x2 - x1 - 1
    gapEndIndex = 1
    for i in range(len(occupiedList) - 1):
        newGap = occupiedList[i+1] - occupiedList[i] - 1
        if (newGap > maxGap):
            x1, x2 = occupiedList[i], occupiedList[i+1]
            gapEndIndex = i + 1
            maxGap = newGap
    return gapEndIndex, x1, x2, maxGap

def enterStall(occupiedList, gapEndIndex, x1, maxGap):
    stallNo = x1 + math.ceil(maxGap / 2)
    occupiedList.insert(gapEndIndex, stallNo)
    return stallNo

def gapMaxMin(x1, x2, stallNo):
    right = x2 - stallNo - 1
    left = stallNo - x1 - 1
    return max(left, right), min(left, right)

def main(n, k):
    a = [0,n+1]
    i = 0
    while (i < k):
        gaps = findGap(a)
        gapEndIndex, x1, x2, maxGap = gaps[0], gaps[1], gaps[2], gaps[3]
        newStallNo = enterStall(a, gapEndIndex, x1, maxGap)
        GapsMinMaxAnswers = gapMaxMin(x1, x2, newStallNo)
        i+=1
    return GapsMinMaxAnswers

# reading and writing files
answers = open(fileout, 'w')
with open(filein) as file:
    numlist = file.readlines()
    nitems = int(numlist[0])
    for i in range(1,nitems+1):
        inputStr = numlist[i].strip('\n').split()
        n = int(inputStr[0])
        k = int(inputStr[1])
        mainAnswer = main(n, k)
        answers.write("case #" + str(i) + ": " + str(mainAnswer[0]) + ' ' + str(mainAnswer[1]) + '\n')
