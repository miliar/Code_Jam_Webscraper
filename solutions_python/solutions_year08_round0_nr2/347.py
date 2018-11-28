# <beyer.andrew@gmail.com>
import sys

inputFile = open(sys.argv[1])

def ReadStrLine():
    return inputFile.readline().rstrip("\r\n")

def ReadIntLine():
    return int(inputFile.readline().rstrip("\r\n"))

def HMToMins(hm):
    hours,minutes = hm.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours*60+minutes

endOfDay = HMToMins("23:59")

def DoCase():
    turnaroundTime = ReadIntLine()
    numA,numB = map(int, ReadStrLine().split())
    departsA = []
    departsB = []
    readyA = []
    readyB = []

    for i in range(numA):
        depart,arrive = map(HMToMins, ReadStrLine().split())
        departsA.append(depart)
        ready = arrive + turnaroundTime
        if ready <= endOfDay:
            readyB.append(ready)
    
    for i in range(numB):
        depart,arrive = map(HMToMins, ReadStrLine().split())
        departsB.append(depart)
        ready = arrive + turnaroundTime
        if ready <= endOfDay:
            readyA.append(ready)

    departsA.sort()
    departsB.sort()
    readyA.sort()
    readyB.sort()
    
    startA = startB = 0
    for depart in departsA:
        if readyA and readyA[0] <= depart:
            readyA[0:1]=[]
        else:
            startA += 1
    for depart in departsB:
        if readyB and readyB[0] <= depart:
            readyB[0:1]=[]
        else:
            startB += 1

    return "%d %d" % (startA, startB)


caseCount = ReadIntLine()
for case in range(1, caseCount+1):
    print "Case #%d:" % case, DoCase()
