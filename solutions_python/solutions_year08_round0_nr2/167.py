#!/usr/bin/python

import sys

next = sys.stdin.readline
numberOfCases = int(next())
for caseNumber in range(1,numberOfCases+1):
    # Process a case
    turnaround = int(next())
    numbersOfTrips = next().split()
    nAtoB = int(numbersOfTrips[0])
    nBtoA = int(numbersOfTrips[1])
    leaveA = []
    leaveB = []
    readyAtA = []
    readyAtB = []
    for i in range(0,nAtoB):
        trip = next()[:-1]
        trip = trip.split()
        trips = trip[0].split(':') + trip[1].split(':')
        leaveA.append(int(trips[0])*60+int(trips[1]))
        readyAtB.append(int(trips[2])*60+int(trips[3])+turnaround)
    for i in range(0,nBtoA):
        trip = next()[:-1]
        trip = trip.split()
        trips = trip[0].split(':') + trip[1].split(':')
        leaveB.append(int(trips[0])*60+int(trips[1]))
        readyAtA.append(int(trips[2])*60+int(trips[3])+turnaround)
    # We sort the lists
    readyAtA.sort()
    readyAtB.sort()
    leaveA.sort()
    leaveB.sort()
    trainsAtA = 0
    trainsAtB = 0
    # We compute the number of trains we need at A
    while len(leaveA) > 0:
        if len(readyAtA) == 0:
            trainsAtA = trainsAtA + len(leaveA)
            break
        else:
            if leaveA[0] < readyAtA[0]:
                trainsAtA = trainsAtA + 1
            else:
                readyAtA = readyAtA[1:]
            # In any case, we've processed a departure
            leaveA = leaveA[1:]
    # We compute the number of trains we need at B
    while len(leaveB) > 0:
        if len(readyAtB) == 0:
            trainsAtB = trainsAtB + len(leaveB)
            break
        else:
            if leaveB[0] < readyAtB[0]:
                trainsAtB = trainsAtB + 1
            else:
                readyAtB = readyAtB[1:]
            # In any case, we've processed a departure
            leaveB = leaveB[1:]
    print "Case #" + str(caseNumber) + ": " + str(trainsAtA) + " " + str(trainsAtB)
