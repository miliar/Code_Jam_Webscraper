import sys
from collections import deque

inputFile = open(sys.argv[1])

numberOfCases = int(inputFile.readline())

for i in range(numberOfCases):
   (numRides, rideCapacity, numGroups) = [int(x) for x in inputFile.readline().split()]
   groupsInLine = deque([int(x) for x in inputFile.readline().split()])

   runningTotal = 0
   for j in range(numRides):
      groupsOnRide = deque()
      numberOfRiders = 0
      while numberOfRiders < rideCapacity:
         try:
            if groupsInLine[0] + numberOfRiders <= rideCapacity:
               nextGroup = groupsInLine.popleft()
               numberOfRiders += nextGroup
               runningTotal += nextGroup
               groupsOnRide.append(nextGroup)
            else:
               break
         except:
            break
      groupsInLine.extend(groupsOnRide)

   print "Case #" + str(i+1) + ": " + str(runningTotal)
