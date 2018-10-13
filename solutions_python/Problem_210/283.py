#!/usr/bin/python
import sys
class AttDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def processCase(case, caseNum):
    allActs = sorted(case.camActs + case.jamActs, key=lambda x: x.start)
    canBad = [[], []]
    canGood = 0
    changes = 0
    times = [0, 0]
    if allActs[0].pers is allActs[-1].pers:
        canBad[allActs[0].pers].append(1440 - allActs[-1].end + allActs[0].start)
        times[allActs[0].pers] += 1440 - allActs[-1].end + allActs[0].start
    else:
        canGood += 1440 - allActs[-1].end + allActs[0].start
        changes += 1
    ind = 0
    while ind < len(allActs) - 1:
        try:
            otherPersonInd = allActs.index([x for x in allActs if x.start >= allActs[ind].end and x.pers is not allActs[ind].pers][0])
        except:
            times[allActs[ind].pers] += allActs[-1].end - allActs[ind].start
            for i in range(ind, len(allActs) - 1):
                canBad[allActs[ind].pers].append(allActs[i+1].start - allActs[i].end)
            break
        canGood += allActs[otherPersonInd].start - allActs[otherPersonInd - 1].end
        for i in range(ind, otherPersonInd):
            canBad[allActs[ind].pers].append(allActs[i+1].start - allActs[i].end)
        times[allActs[ind].pers] += allActs[otherPersonInd-1].end - allActs[ind].start
        ind = otherPersonInd
        changes += 1
    canBad[0].sort(reverse=1)
    canBad[1].sort(reverse=1)
    while times[0] > 720:
        changes += 2
        times[0] -= canBad[0][0]
        del canBad[0][0]
    while times[1] > 720:
        changes += 2
        times[1] -= canBad[1][0]
        del canBad[1][0]
    print("Case #%d: %d" % (caseNum, changes))

with open(sys.argv[1]) as f:
    data = f.read().split('\n')
    i = 0
    testCaseNum = int(data[i])
    i += 1
    testCases = []
    for _ in range(testCaseNum):
        numCameron, numJamie = [int(x) for x in data[i].split(' ')]
        i += 1
        camActs = []
        for _ in range(numCameron):
            start, end = [int(x) for x in data[i].split(' ')]
            i += 1
            dic = AttDict()
            dic.start = start
            dic.end = end
            dic.ln = end - start
            dic.pers = 0
            camActs.append(dic)
        jamActs = []
        for _ in range(numJamie):
            start, end = [int(x) for x in data[i].split(' ')]
            i += 1
            dic = AttDict()
            dic.start = start
            dic.end = end
            dic.ln = end - start
            dic.pers = 1
            jamActs.append(dic)
        dic = AttDict()
        dic.numCameron = numCameron
        dic.numJamie = numJamie
        dic.camActs = camActs
        dic.jamActs = jamActs
        testCases.append(dic)
    num = 0
    for case in testCases:
        num += 1
        processCase(case, num)
