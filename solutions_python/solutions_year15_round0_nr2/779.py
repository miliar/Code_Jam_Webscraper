import sys
import functools
import math

# 6 / 3 => 5
# 6 / 2 => 4

def get_lines():
    return [line.rstrip('\n') for line in sys.stdin]

def numerize(string, splitBy=' '):
    return [int(item) for item in string.split(splitBy)]

def timeit(data, totalSplits):
    return data[-1:][0] + totalSplits

def tooMuchNumber(nb, nbOfNb):
    return ((math.ceil(nb / 2) + nbOfNb) > nb)

def isNineAlone(data, totalSplits):
    data.remove(9)
    data.append(6)
    data.append(3)
    data = sorted(data)
    return data, (totalSplits + 1)

def nextMax(data):
    currentMax = max(data)
    nextMax = 0
    for nb in data:
        if nb > nextMax and nb < currentMax:
            nextMax = nb
    return nextMax

def splitBiggest(data, totalSplits):
    biggest = data[-1:][0]
    biggestCount = data.count(biggest)
    if biggest < 2 or tooMuchNumber(biggest, biggestCount):
        return data, totalSplits

    nmax = nextMax(data)
    if biggest == 9 and biggestCount == 1 and (nmax < 5 or nmax == 0 or nmax == 6):
        return isNineAlone(data, totalSplits)

    totalSplits += biggestCount
    for i in range(0, biggestCount):
        data.remove(biggest)
        data.append(math.ceil(biggest / 2))
        data.append(math.floor(biggest / 2))
    data = sorted(data)
    return data, totalSplits

def isDone(data):
    biggest = data[-1:][0]
    biggestCount = data.count(biggest)
    if biggest < 2 or tooMuchNumber(biggest, biggestCount):
        return True
    return False

lines = get_lines()
nbCases = int(lines.pop(0))

exit_at = 62

for case in range(0, nbCases):
    nbNonEmptyDiner = int(lines.pop(0))
    cakes = sorted(numerize(lines.pop(0)))
    totalSplits = 0
    minutes = timeit(cakes, totalSplits)
    # if case == exit_at:
    #     print('Original: ', cakes, minutes)
    while isDone(cakes) is False:
        cakes, totalSplits = splitBiggest(cakes, totalSplits)
        if minutes > timeit(cakes, totalSplits):
            minutes = timeit(cakes, totalSplits)
        # if case == exit_at:
        #     print(cakes, totalSplits, timeit(cakes, totalSplits))
    print("Case #", (case + 1), ": ", minutes, sep="")
    # if case == exit_at:
    #     sys.exit(1)
