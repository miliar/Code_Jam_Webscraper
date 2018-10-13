import sys

def IsAllHappy(pancakes):
    happy = True
    for c in pancakes:
        if c == '-':
            happy = False
            break
    return happy

def GetIndexOfFirstUnhappy(pancakes):
    index = 0
    for i, c in enumerate(pancakes):
        if c == '-':
            index = i
            break
    return index

def FlipPancakes(pancakes, index, runLength):
    for i in range(index, index+runLength):
        if(pancakes[i] == '+'):
            pancakes[i] = '-'
        else:
            pancakes[i] = '+'
    return pancakes

inputStrings = open('A-large.in', 'r').read().splitlines()
caseNum = int(inputStrings[0])
outString = ""

lineNum = 1;
for case in range(1,caseNum+1):
    print(case)
    inData = inputStrings[lineNum].split(' ')
    pancakeString = list(inData[0])
    flipperCount = int(inData[1])
    lineNum += 1

    flipCount = 0
    while not IsAllHappy(pancakeString):
        nextFlipIndex = GetIndexOfFirstUnhappy(pancakeString)
        if(nextFlipIndex > len(pancakeString) - flipperCount):
            flipCount = "IMPOSSIBLE"
            break
        else:
            pancakeString = FlipPancakes(pancakeString, nextFlipIndex, flipperCount)
            flipCount += 1

    outString += "Case #" + str(case) + ": " + str(flipCount)
    if(case < caseNum):
        outString += "\n"

fileOut = open('A-large.out', 'w')
fileOut.write(outString)
fileOut.close()