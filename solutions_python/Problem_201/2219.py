import heapq
import math

def getStalls(N, K):
    K -= 1

    i = 0
    h = []
    heapq.heappush(h, (-1 * N, 0, N - 1))
    split_point = []
    while i < K:
        size, low, high = heapq.heappop(h)
        mid = int((low + high) / 2)
        lsize = mid - low
        rsize = high - mid
        split_point.append(mid)
        heapq.heappush(h, (-1 * lsize, low, mid - 1))
        heapq.heappush(h, (-1 * rsize, mid + 1, high))
        # print split_point
        i += 1

    stall = [0] * N
    for i in split_point:
        stall[i] = 1

    lDis = 0
    rDis = 0

    stalls = ''.join(str(e) for e in stall)

    stalls = '1' + stalls + '1'

    # print(stalls)

    lDis = 0
    rDis = 0
    maxZeros = max(stalls.split("1"))
    indexMaxZeros = stalls.index(maxZeros)
    realIndex = 0

    if (len(maxZeros) % 2 == 0):
        realIndex = indexMaxZeros + int(len(maxZeros) / 2) - 1
    else:
        realIndex = indexMaxZeros + int(len(maxZeros) / 2)

    # print(realIndex)

    lDis = stalls[realIndex - 1::-1].index('1')
    rDis = stalls[realIndex + 1:len(stalls)].index('1')

    # print("{0} {1}".format(max(lDis, rDis), min(lDis, rDis)))


    return "{0} {1}".format(max(lDis, rDis), min(lDis, rDis))


def processMany():
    with open("/Users/ChesterAiGo/Desktop/c2.txt") as Doc:
        lines = [x.strip() for x in Doc.readlines()]

    for i in range(len(lines)):
        N = int(lines[i].split(" ")[0])
        K = int(lines[i].split(" ")[1])
        print("Case #{0}: {1}".format(i + 1, getStalls(N, K)))

processMany()
