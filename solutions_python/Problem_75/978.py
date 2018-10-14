#Tested locally with Python 2.6.6 on OS X 10.6.7
import math

input = open('B-large.in','r')
output = open('B-large.out','w')
T = int(input.next())

for i in range(0,T):
    baseEls = {}
    opp = {}
    numsonein = input.next().split(' ')
    C = int(numsonein[0])
    for j in range(0,C):
        curString = numsonein[1+j]
        baseEls[curString[0:2]] = curString[2]
        baseEls[curString[0:2][::-1]] = curString[2]
    D = int(numsonein[C+1])
    for j in range(0,D):
        curString = numsonein[C+1+j+1]
        if opp.has_key(curString[0]):
            opp[curString[0]] = opp[curString[0]]+curString[1]
        else:
            opp[curString[0]] = curString[1]
        if opp.has_key(curString[1]):
            opp[curString[1]]= opp[curString[1]]+curString[0]
        else:
            opp[curString[1]] = curString[0]
    N = int(numsonein[C+1+D+1])

    curList = []
    myList = numsonein[C+1+D+1+1]
    for j in range(0,N):
        nextOne = myList[j]
        curList.append(nextOne)
        while True:
            if curList == []:
                break
            if len(curList) == 1:
                break
            else:
                curKey = curList[-1]+curList[-2]
                if baseEls.has_key(curKey):
                    curList = curList[0:-2]
                    curList.append(baseEls[curKey])
                else:
                    break
        for k in range(0,len(curList)):
            for m in range(k,len(curList)):
                if opp.has_key(curList[k]):
                    if opp[curList[k]].find(curList[m]) != -1:
                        curList = []
                        break

    output.write("Case #"+str(i+1)+": [")
    for j in range(0,len(curList)):
        output.write(curList[j])
        if j != len(curList)-1:
            output.write(', ')
    output.write("]\n")
