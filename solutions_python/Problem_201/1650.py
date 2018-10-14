import math


def solveSmall2(n, k):

    h = math.floor(math.log(k, 2))
    E = n - (math.pow(2, h) - 1)

    bucketSize = math.floor(E / math.pow(2, h))
    bucketSizeOfExtra = E % math.pow(2, h)

    positionOnLevel = k - (math.pow(2, h) - 1)

    lenOfSegment = bucketSize
    if positionOnLevel <= bucketSizeOfExtra:
        lenOfSegment = bucketSize + 1

    x = 1
    y = lenOfSegment
    a = int((x + y) / 2)

    if a - x >= y - a:
        return a - x, y - a

    return y - a, a - x


def solveSmall1(n, k):
    indexPairList = [(1, n)]

    for n in range(1, k):

        bestPair = indexPairList.pop(0)

        x = bestPair[0]
        y = bestPair[1]

        a = int((x + y) / 2)

        if x < a:
            indexPairList.append((x, a - 1))
        if a < y:
            indexPairList.append((a + 1, y))

        indexPairList.sort(key=lambda x: (x[1] - x[0] + 1, x[0]), reverse=True)

    bestPair = indexPairList.pop(0)

    x = bestPair[0]
    y = bestPair[1]
    a = int((x + y) / 2)

    if a - x >= y - a:
        return a - x, y - a

    return y - a, a - x


# inputFile = open('C-small-1-attempt0.in', 'r')
# outputFile = open('C-small-1-attempt0.out', 'w')

inputFile = open('C-small-2-attempt1.in', 'r')
outputFile = open('C-small-2-attempt1.out', 'w')

#inputFile = open('C-small.in', 'r')
#outputFile = open('C-small.out', 'w')

testCase = int(inputFile.readline())
for case in range(1, testCase + 1):
    N, K = [int(x) for x in inputFile.readline().split()]
    result = solveSmall2(N, K)
    outputFile.write('Case #{}: {} {}\n'.format(case, result[0], result[1]))

inputFile.close()
outputFile.close()
