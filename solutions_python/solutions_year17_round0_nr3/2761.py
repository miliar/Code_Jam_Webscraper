
def getMin(stalls, stall):
    offset = 1
    while (True):
        if (stall - offset < 0 or stall + offset >= len(stalls)):
            return offset - 1
        if stalls[stall - offset] or stalls[stall + offset]:
            return offset - 1

        offset += 1

def getMax(stalls, stall):
    offsetRight = 1
    offsetLeft = 1
    while (True):
        if (stall - offsetLeft < 0 or stalls[stall - offsetLeft]):
            break
        offsetLeft += 1

    while (True):
        if (stall + offsetRight >= len(stalls) or stalls[stall + offsetRight]):
            break
        offsetRight += 1

    return max(offsetLeft, offsetRight) - 1


T = int(input())
case = 0

try:
    while True:
        line = input()
        case += 1
        s = line.split()

        N = int(s[0])
        K = int(s[1])

        stalls = [False] * N
        indexThatChanged = 0

        for i in range(K):
            # STEP 1
            minDist = [0] * len(stalls)

            for stall in range(len(stalls)):
                if (stalls[stall]): # If occupied, do not even consider
                    minDist[stall] = -1
                else:
                    minDist[stall] = getMin(stalls, stall)

            maxMinDist = max(minDist)
            minDistIndices = [i for i, j in enumerate(minDist) if j == maxMinDist]

            if (len(minDistIndices) == 1): # If only one stall that has the highest minimal distance
                stalls[minDistIndices[0]] = True
                indexThatChanged = minDistIndices[0]
                continue

            # STEP 2
            maxDist = [-1] * len(stalls)
            for stall in minDistIndices:
                maxDist[stall] = getMax(stalls, stall)

            maxMaxDist = max(maxDist)
            maxDistIndices = [i for i, j in enumerate(maxDist) if j == maxMaxDist]

            stalls[maxDistIndices[0]] = True
            indexThatChanged = maxDistIndices[0]

        print("Case #{}: {} {}".format(case, getMax(stalls, indexThatChanged), getMin(stalls, indexThatChanged)))

except EOFError:
    pass
