#!/usr/bin/python
from string import atoi

def parsedate(s):
    return atoi(''.join(s.split(':')))

def comparedepartures(x,y):
    x = parsedate(x[0])
    y = parsedate(y[0])
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1

def getnumtrains(abdepartures,badepartures,turnaround):
    for btrain in badepartures:
        for atrain in abdepartures:
            if parsedate(btrain[1]) + turnaround <= parsedate(atrain[0]):
                abdepartures.remove(atrain)
                break
    return len(abdepartures)

numcases = input()
for case in range(numcases):
    turnaround = input()
    departures = raw_input().split(' ')
    numabdepartures = atoi(departures[0])
    numbadepartures = atoi(departures[1])
    abdepartures = []
    badepartures = []
    for i in range(numabdepartures):
        abdepartures.append(raw_input().split(' '))
    for i in range(numbadepartures):
        badepartures.append(raw_input().split(' '))
    abdepartures.sort(comparedepartures)
    badepartures.sort(comparedepartures)
    #make deep copies [:]
    abtrains = getnumtrains(abdepartures[:],badepartures[:],turnaround)
    batrains = getnumtrains(badepartures[:],abdepartures[:],turnaround)
    print ''.join(['Case #',str(case+1),': ',str(abtrains),' ',str(batrains)])
