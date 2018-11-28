#!/usr/bin/env python

def scheduleTime(strTime):
    [hh, mm] = strTime.split(':')
    return 60*int(hh) + int(mm)

import sys

argv = sys.argv[1:]
inFile = open(argv[0] + '.in', 'rb')
outFile = open(argv[0] + '.out', 'wb')


n = int(inFile.readline())
for testCase in xrange(1, n+1):
    turnaround = int(inFile.readline())
    
    aArrive = []
    bArrive = []
    aDepart = []
    bDepart = []
    [nA, nB] = map(int, inFile.readline().split())
    for i in xrange(nA):
        [depart, arrive] = inFile.readline().split()
        aDepart.append(scheduleTime(depart))
        bArrive.append(scheduleTime(arrive))
    for i in xrange(nB):
        [depart, arrive] = inFile.readline().split()
        bDepart.append(scheduleTime(depart))
        aArrive.append(scheduleTime(arrive))
    aArrive.sort()
    bArrive.sort()
    aDepart.sort()
    bDepart.sort()
    
    nA = 0
    nB = 0
    for time in aDepart:
        if len(aArrive) == 0 or aArrive[0] + turnaround > time:
            nA += 1
        else:
            del aArrive[0]
    for time in bDepart:
        if len(bArrive) == 0 or bArrive[0] + turnaround > time:
            nB += 1
        else:
            del bArrive[0]
    
    outFile.write('Case #%i: %i %i\n' % (testCase, nA, nB))

outFile.close()
inFile.close()