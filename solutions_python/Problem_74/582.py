import sys

def slove():
    icase = int(input())
    for i in range(icase):
        seq = input().split()[1:]
        btnDict = {'O':1, 'B':1}
        stepDict = {'O':0, 'B':0}
        prevBot = 'B'
        for j in range(len(seq)//2):
            currRot = seq[j*2]
            currRotBtn = int(seq[j*2 + 1])
            if prevBot == currRot:
                stepDict[currRot] += abs(currRotBtn - btnDict[currRot]) + 1
            else:
                stepDict[currRot] = max(stepDict[currRot] + abs(currRotBtn - btnDict[currRot]), stepDict[prevBot]) + 1
                prevBot = currRot
            btnDict[currRot] = currRotBtn
        print('Case #%d:'%(i+1),max(stepDict.values()))

slove()    