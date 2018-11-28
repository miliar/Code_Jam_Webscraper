import os
import copy
import math

# Create Output file
f = open('dataOut.txt', "w")
f.close()


# Read Input file
f = open('B-small-attempt0.in', "rb")
numOfTestCases = f.readline()

for i in range(0,int(numOfTestCases)):
    currentData = f.readline()
    currentData = currentData.split()
    numOfCombos = currentData.pop(0)
    numOfCombos = int(numOfCombos)
    validCombos = range(2*numOfCombos)
    for j in range(0,numOfCombos):
        temp = currentData.pop(0)
        tempList = list(temp)
        validCombos[j] = tempList
        j=j+1
        tempList = copy.deepcopy(tempList)
        temp2 = tempList.pop(0)
        tempList.insert(1,temp2)
        validCombos[j] = tempList

    numOfInvalid = currentData.pop(0)
    numOfInvalid = int(numOfInvalid)
    invalidCombos = range(2*numOfInvalid)
    for j in range(0,numOfInvalid):
        temp = currentData.pop(0)
        tempList = list(temp)
        invalidCombos[j] = tempList
        j=j+1
        tempList = copy.deepcopy(tempList)
        temp2 = tempList.pop(0)
        tempList.insert(1,temp2)
        invalidCombos[j] = tempList

    numInSeries = currentData.pop(0)
    numInSeries = int(numInSeries)
    toInvoke = currentData.pop(0)
    toInvoke = list(toInvoke)

    invoked = []
    while(numInSeries != 0):
        added = False
        toAdd = toInvoke.pop(0)
        if (len(invoked) < 1):
            invoked.append(toAdd)
            added = True
        if (added == False):
            for k in range(0,len(validCombos)):
                myLength = len(invoked) - 1
                toCompare = invoked.pop(myLength)
                if(validCombos[k][0] == toAdd and validCombos[k][1] == toCompare):
                    invoked.append(validCombos[k][2])
                    added = True
                    break
                invoked.append(toCompare)
        if (added == False):
            for k in range(0,len(invoked)):
                toCompare = invoked[k]
                for l in range(0,len(invalidCombos)):
                    if(invalidCombos[l][0] == toCompare and invalidCombos[l][1] == toAdd):
                        invoked = []
                        added = True
                        break
                if (added == True):
                    break
        if (added == False):
            invoked.append(toAdd)
        numInSeries = numInSeries-1
    g = open('dataOut.txt', "a")
    caseNum =  i + 1
    g.write("Case #" + repr(caseNum) + ": [")
    for k in range(0,len(invoked)):
        g.write(invoked[k])
        if (k != len(invoked)-1):
            g.write(", ")
    g.write("]\n")
    g.close()
f.close()
