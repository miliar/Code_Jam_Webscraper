
def runSolution():
    baseFileName = 'A-large'
    inputFile = open('%s.in' % baseFileName, 'r')
    outputFile = open('%s.out' % baseFileName, 'w')
    numberOfCases = int(inputFile.readline())

    for caseNumber in range(numberOfCases):
        result = solveCase(inputFile)
        answerLine = "Case #%d: %s\n" % (caseNumber + 1, result)
        print answerLine
        outputFile.write(answerLine)

    inputFile.close();
    outputFile.close();

def solveCase(inputFile):
    groupsAndPieces = inputFile.readline().split()
    numberOfGroups = int(groupsAndPieces[0])
    pieces = int(groupsAndPieces[1])
    print '%d groups and %d pieces' % (numberOfGroups, pieces)
    groups = list(map(lambda x: int(x) % pieces, inputFile.readline().split()))
    print groups
    groups = [x for x in groups if x > 0]
    groups.sort()
    groups = groups[::-1]
    print groups
    staleCount = 0

    i = 0
    while i < len(groups):
        A = groups[i]
        j = i + 1
        while j < len(groups):
            B = groups[j]
            if ((A + B) % pieces == 0):
                staleCount += 1
                groups.pop(j)
                groups.pop(i)
                i -= 1
                break
            j += 1
        i += 1
    print groups

    i = 0
    while i < len(groups):
        A = groups[i]
        j = i + 1
        done = False
        while j < len(groups) and not done:
            B = groups[j]
            k = j + 1
            while k < len(groups) and not done:
                C = groups[k]
                if ((A + B + C) % pieces == 0):
                    staleCount += 2
                    groups.pop(k)
                    groups.pop(j)
                    groups.pop(i)
                    i -= 1
                    done = True
                k += 1
            j += 1
        i += 1
    print groups

    if pieces > 3:
        i = 0
        while i < len(groups):
            A = groups[i]
            j = i + 1
            done = False
            while j < len(groups) and not done:
                B = groups[j]
                k = j + 1
                while k < len(groups) and not done:
                    C = groups[k]
                    l = k + 1
                    while l < len(groups) and not done:
                        D = groups[l]
                        if ((A + B + C + D) % pieces == 0):
                            staleCount += 3
                            groups.pop(l)
                            groups.pop(k)
                            groups.pop(j)
                            groups.pop(i)
                            i -= 1
                            done = True
                        l += 1
                    k += 1
                j += 1
            i += 1
    print groups

    result = numberOfGroups - staleCount - max(0, len(groups) - 1) # The first group is fresh for free
    return str(result)

runSolution()
