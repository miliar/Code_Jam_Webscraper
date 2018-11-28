filename = "B-small-attempt2.in"

f = open(filename, "r")
numTestCases = f.readline()

def deductPancake(pancakeDist):
    pancakeDistCopy = list(pancakeDist)
    i = 0
    while i < len(pancakeDistCopy):
        if pancakeDistCopy[i] > 0:
            pancakeDistCopy[i] -= 1
        i += 1
    j = 0
    return filter(lambda a: a != 0, pancakeDistCopy)

def changeDist(pancakeDist, maxPancake, amt):
    pancakeDistCopy = list(pancakeDist)
    pancakeDistCopy.remove(maxPancake)
    pancakeDistCopy.append(amt)
    pancakeDistCopy.append(maxPancake - amt)
    return pancakeDistCopy

def recursePancakes(pancakeDist, minSoFar, originalMax):
    # print str(pancakeDist) + ", min: " + str(minSoFar + max(pancakeDist))
    remainingPancakesAllOne = True
    for i in range(len(pancakeDist)):
        if pancakeDist[i] > 1:
            remainingPancakesAllOne = False

    if remainingPancakesAllOne:
        return 1 + minSoFar
    elif minSoFar > originalMax:
        return originalMax
    else:
        listDist = []
        maxPancake = max(pancakeDist)
        for i in range(1, maxPancake / 2 + 1):
            listDist.append(recursePancakes(changeDist(pancakeDist, maxPancake, i), minSoFar + 1, originalMax))
        return min(min(listDist),
            recursePancakes(deductPancake(pancakeDist), minSoFar + 1, originalMax))

for testCase in range(int(numTestCases)):

    nonEmptyDiners = int(f.readline())
    pancakeDist = [int(p) for p in f.readline().split()]

    minutes = recursePancakes(pancakeDist, 0, max(pancakeDist))

    # print "Original Dist: " + str(pancakeDist)
    print "Case #" + str(testCase + 1) + ": " + str(minutes)

