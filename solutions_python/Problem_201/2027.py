import sys
import math

class StallDistance:
    right = 0
    left = 0

inputStrings = open('C-small-1-attempt0.in', 'r').read().splitlines()
caseNum = int(inputStrings[0])
outString = ""

lineNum = 1;
for case in range(1,caseNum+1):
    print(case)
    inData = inputStrings[lineNum].split(' ')
    lineNum += 1

    stallCount = int(inData[0])
    peopleCount = int(inData[1])

    leftPerson = [0, stallCount]
    stalls = [leftPerson]
    lastIndex = 0
    for p in range(0, peopleCount):
        #TODO(ken): optimize this
        maxLeft = max(stalls, key=lambda item:item[0])
        maxRight = max(stalls, key=lambda item:item[1])


        # maxLeft = max(stalls, key=lambda item:item[0])[0]
        # maxRight = max(stalls, key=lambda item:item[1])[1]

        if maxLeft[0] >= maxRight[1]:
            right = False
            maxVal = maxLeft[0]
            indexToAdd = stalls.index(maxLeft)
            oldIndex = indexToAdd + 1
        else:
            right = True
            maxVal = maxRight[1]
            indexToAdd = stalls.index(maxRight) + 1
            oldIndex = indexToAdd - 1

        newLeft = math.ceil(maxVal / 2)
        newRight = maxVal - newLeft
        newLeft = newLeft - 1
        stalls.insert(indexToAdd, [newLeft, newRight])
        lastIndex = indexToAdd

        if right:
            stalls[indexToAdd - 1][1] = newLeft
            if (indexToAdd + 1) < len(stalls):
                stalls[indexToAdd + 1][0] = newRight
        else:
            if (indexToAdd - 1) >= 0:
                stalls[indexToAdd - 1][1] = newLeft
            stalls[indexToAdd + 1][0] = newRight

        x = 0


    maxOut = max(stalls[lastIndex])
    minOut = min(stalls[lastIndex])
    outString += "Case #" + str(case) + ": " + str(maxOut) + " " + str(minOut)
    if(case < caseNum):
        outString += "\n"

fileOut = open('C-small-1-attempt0.out', 'w')
fileOut.write(outString)
fileOut.close()