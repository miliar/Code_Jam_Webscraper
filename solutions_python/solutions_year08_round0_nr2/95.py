import sys
from heapq import *

class Trip:
    def __init__(self, start, end, origin, taTime):
        self.start = toMinutes(start)
        self.end = toMinutes(end) + taTime
        self.origin = origin

    def __cmp__(self, trip):
        return cmp(self.end, trip.end)


def toMinutes(timeStr):
    hour = int(timeStr[0:2])
    minute = int(timeStr[3:5])
    return 60*hour + minute

inFile = sys.stdin
#inFile = open("A-small-attempt1.in", 'r')

numCases = int(inFile.readline())
for caseNum in range(numCases):

    taTime = int(inFile.readline())
    
    NA, NB = inFile.readline().split()
    numA = int(NA)
    numB = int(NB)

    trips = []
    for i in range(numA):
        startTime, endTime = inFile.readline().split()
        trips.append(Trip(startTime, endTime, 0, taTime))

    for i in range(numB):
        startTime, endTime = inFile.readline().split()
        trips.append(Trip(startTime, endTime, 1, taTime))

    trips.sort(lambda trip1, trip2: cmp(trip1.start, trip2.start))

    numStarters = [0]*2
    numAvailable = [0]*2

    arrivals = []

    tripIdx = 0
    while True:
        if tripIdx == len(trips):
            break
        
        if len(arrivals) == 0 or arrivals[0].end > trips[tripIdx].start:
            trip = trips[tripIdx]
            if numAvailable[trip.origin] == 0:
                numStarters[trip.origin] += 1
            else:
                numAvailable[trip.origin] -= 1

            heappush(arrivals, trip)
            tripIdx += 1
        else:
            arrival = heappop(arrivals)
            numAvailable[1 - arrival.origin] += 1

    print "Case #%d: %d %d" % (caseNum + 1, numStarters[0], numStarters[1])
                
