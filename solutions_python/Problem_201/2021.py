from heapq import heappush, heappop
from math import ceil

def getLeftRight(stallList, index):
    length = len(stallList)
    numStallsRight = 0
    for i in range(index+1, length):
        if(stallList[i] != 1):
            numStallsRight += 1
        else:
            break
    stallRightTuple = (numStallsRight*-1, index)

    numStallsLeft = 0
    leftIndex = 0
    for i in range(index-1, 0, -1):
        if(stallList[i] != 1):
            numStallsLeft += 1
        else:
            leftIndex = i
            break
    stallLeftTuple = (numStallsLeft*-1, leftIndex)

    return [stallLeftTuple, stallRightTuple]


numCases = int(input())
for i in range(1, numCases+1):
    stalls, people = [int(s) for s in raw_input().split(' ')]
    nextStall = []
    heappush(nextStall, ((stalls*-1), 0))
    stallList = [0] * (stalls+2)
    stallList[0] = 1
    stallList[stalls+1] = 1

    lastTuple = ()

    for person in xrange(people):
        bestTuple = heappop(nextStall)
        index = bestTuple[1]
        numStalls = bestTuple[0]*-1

        nextStallIndex = int(index + ceil(numStalls/2.0))
        stallList[nextStallIndex] = 1
        nextTuples = getLeftRight(stallList, nextStallIndex)
        leftVal = nextTuples[0][0] * -1
        rightVal = nextTuples[1][0] * -1
        lastTuple = (leftVal, rightVal)
        if (leftVal != 0):
            heappush(nextStall, nextTuples[0])
        if (rightVal != 0):
            heappush(nextStall, nextTuples[1])

    print("Case #{}: {} {}").format(i, max(lastTuple), min(lastTuple))
