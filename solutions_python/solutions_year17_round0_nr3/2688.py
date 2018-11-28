def main():
    fileInput = open("input.txt", 'r')
    intCaseCount = int(fileInput.readline())
    alstCases = [strCase.split(" ") for strCase in fileInput.readlines()]
    fileInput.close()
    fileOutput = open("output.txt", 'w')
    for intCaseIndex in range(intCaseCount):
        print(solveCase(int(alstCases[intCaseIndex][0]), int(alstCases[intCaseIndex][1]), intCaseIndex + 1))
        fileOutput.write(solveCase(int(alstCases[intCaseIndex][0]), int(alstCases[intCaseIndex][1]), intCaseIndex + 1) + "\n")
    fileOutput.close()


def solveCase(n, k, intCaseCount):
    aintLocations = [1, n + 2]
    while k != 0:
        aintLocations, intIndex = addMan(aintLocations)
        k -= 1
    aintResult = findDiffs(aintLocations, intIndex)
    return "Case #{0}: {1} {2}".format(intCaseCount, aintResult[0], aintResult[1])


def addMan(aintLocations):
    intMaxDiffIndex = findMaxDiffIndex(aintLocations)
    newLocation = (aintLocations[intMaxDiffIndex] + aintLocations[intMaxDiffIndex + 1]) // 2
    aintLocations = aintLocations[:intMaxDiffIndex + 1] + [newLocation] + aintLocations[intMaxDiffIndex + 1:]
    return aintLocations, intMaxDiffIndex + 1
    

def findMaxDiffIndex(aintLocations):
    intMaxDiff = 0
    intMaxDiffIndex = 0
    for intIndex in range(len(aintLocations) - 1):
        intCurrDiff = aintLocations[intIndex + 1] - aintLocations[intIndex]
        if intCurrDiff > intMaxDiff:
            intMaxDiff = intCurrDiff
            intMaxDiffIndex = intIndex
    return intMaxDiffIndex


def findDiffs(aintLocations, intIndex):
    assert(0 < intIndex < len(aintLocations) - 1)
    intLeft = aintLocations[intIndex] - aintLocations[intIndex - 1] - 1
    intRight = aintLocations[intIndex + 1] - aintLocations[intIndex] - 1
    intMaxDiff = max(intLeft, intRight)
    intMinDiff = min(intLeft, intRight)
    return [intMaxDiff, intMinDiff]

if __name__ == "__main__":
    main()
