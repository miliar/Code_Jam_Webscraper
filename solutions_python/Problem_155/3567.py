#!/usr/bin

import io

def getMembersStood(Sis, indexLimit):
    total = 0
    i = 0
    for value in Sis:
        if i is indexLimit:
            continue
        total = total + int(value)
        i = i + 1
    return total


f = open('StandingOvationData.txt', 'r')
nCases = int(f.readline())
cases = []
sMax = []
sValues = []
result = ""
for line in f:
    cases.append(line.replace("\n",""))
for case in cases:
    sMax.append(int(case.split(" ")[0]))
    sValues.append(case.split(" ")[1])
for c in range(0,nCases):
    Sis = []
    indexValue = 0
    friends = 0
    membersStoodBefore = 0
    for v in sValues[c]:
        Sis.append(int(v))
    for value in Sis:
        if indexValue == 0 and value == 0:
            friends = friends + 1
            Sis[indexValue] = Sis[indexValue] + 1 
        membersStoodBefore = getMembersStood(Sis, indexValue)
        if membersStoodBefore >= indexValue:
            pass
        else:
            friends = friends + (indexValue - membersStoodBefore)
            Sis[indexValue]  = Sis[indexValue] + (indexValue - membersStoodBefore)
        indexValue = indexValue + 1
    result = result + "Case #%s: %s" % (c + 1,friends) + "\n"
result = result[:-1]
print(result)

ouput = open('ResultStandingOvation.txt','w')
ouput.write(result)

