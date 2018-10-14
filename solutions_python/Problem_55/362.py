import os
import sys
import re

def scheduleRide(currIndex, groupSizeArray, capacity):
    currCapacity = groupSizeArray[currIndex]
    groupCount = len(groupSizeArray)
    newIndex = (currIndex+1)%groupCount
    while(currIndex != newIndex):
        if((currCapacity + groupSizeArray[newIndex])>capacity):
            return((newIndex,currCapacity))
        currCapacity += groupSizeArray[newIndex]
        newIndex = (newIndex+1)%groupCount
    #end while
    return((newIndex,currCapacity))

def findEurosEarnt(caseCount, rknInputStr, groupStr):
    rknInputStr = rknInputStr.strip()
    tempArr = re.split("\s+", rknInputStr)
    (rideCount, capacity, groupCount) = tempArr[0:3]
    rideCount = int(rideCount)
    capacity = int(capacity)
    groupCount = int(capacity)
    ## read in the group sizes
    groupStr = groupStr.strip()
    tempArr = re.split("\s+", groupStr)
    groupSizeArray = []
    for groupStr in tempArr:
        groupSizeArray.append(int(groupStr))
    #end for
    ## actual algo
    groupScheduleMap = {} ## groupIndex --> (euros)
    scheduleLog = []
    currRideCount = 0
    currEurosEarnt = 0
    currIndex = 0
    while((currIndex not in groupScheduleMap) and (currRideCount < rideCount)):
        scheduleLog.append(currIndex)
        (newIndex, eurosEarnt) = scheduleRide(currIndex, groupSizeArray, capacity)
        groupScheduleMap[currIndex] = eurosEarnt
        currRideCount += 1
        currEurosEarnt += eurosEarnt
        currIndex = newIndex
    #end while
    if(currRideCount == rideCount):
        print "Case #"+str(caseCount)+": "+str(currEurosEarnt)
        return
    groupIndex = currIndex
    cycleRideCount = len(scheduleLog) - scheduleLog.index(groupIndex)
    cycleEuros = 0
    for index in range(len(scheduleLog)-1,-1,-1):
         cycleEuros += groupScheduleMap[scheduleLog[index]]
         if(scheduleLog[index] == groupIndex):
             break
    #end for
    cycleCount = (rideCount - currRideCount)/cycleRideCount
    currEurosEarnt += cycleEuros*cycleCount
    remainingRides = rideCount - currRideCount - (cycleCount*cycleRideCount)
    if(remainingRides >0):
        startIndex = scheduleLog.index(groupIndex)
        for index in range(startIndex, startIndex+remainingRides):
            currEurosEarnt += groupScheduleMap[scheduleLog[index]]
    #end if
    print "Case #"+str(caseCount)+": "+str(currEurosEarnt)
    return
#end
    
    
    
    
    

def main():
    filename = sys.argv[1]
    try:
        inp = open(filename, "r")
    except IOError, err:
        print "ERROR: Cannot open the file:" + filename
        sys.exit(2)
    inpCount = inp.readline()
    inpCount = inpCount.strip()
    inpCount = int(inpCount)
    currCaseCount = 1
    while(currCaseCount <= inpCount):
        rknInputStr = inp.readline()
        groupStr = inp.readline()
        findEurosEarnt(currCaseCount, rknInputStr, groupStr)
        currCaseCount += 1

if __name__ == "__main__":
    main()