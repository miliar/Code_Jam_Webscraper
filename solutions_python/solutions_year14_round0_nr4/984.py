__author__ = 'mervinol'
#deceiptful war

outputFile = open("WarOutBig.txt", "a")
inputFile = open("D-large.in", "r")
lines = inputFile.readlines()
inputFile.close()
TestCases = int(lines[0])
startLine = 1

def SolveProblem(linesfed):
    rounds = int(linesfed[0])
    nBlocks = linesfed[1].split("\n")[0]
    kBlocks = linesfed[2].split("\n")[0]
    nBlocks = tuple(float(x) for x in nBlocks.split(" "))
    kBlocks = tuple(float(x) for x in kBlocks.split(" "))
    nSorted = list(sorted(nBlocks))
    kSorted = list(sorted(kBlocks))
    kReverse = list(sorted(kBlocks,reverse=True))

    #play normal War
    nRealWins = 0
    nCheatWins = 0
    for r in range(1,1+rounds):
        smallestN = nSorted.pop(0)
        smallestK = kSorted[0]
        if smallestN > smallestK:
            #       (actual, tells)
            moveN = (smallestN, smallestN)
        else:
            moveN = (smallestN, smallestN)

        biggestK = kSorted[-1]
        if moveN[1] > biggestK:
            moveK = kSorted.pop(0)
        else:
            popK = 0
            breakLoop = False
            for x in range(len(kSorted)):
                if not breakLoop:
                    if kSorted[x] > moveN[1]:
                        popK = x
                        breakLoop = True
            moveK = kSorted.pop(popK)
        if moveN[0]>moveK: nRealWins += 1
        # print "%s. N(%s) %s K(%s)" %(r, moveN, {True: ">", False:"<"}[moveN>moveK], moveK)

    nSorted = list(sorted(nBlocks))
    kSorted = list(sorted(kBlocks))
    #play deceipt War

    # print "N:", nSorted
    # print "K:", kSorted
    for r in range(1,1+rounds):
        #if my smallest would lose, take out his biggest one
        #if my smallest would win, take out his smallest one
        smallestN = nSorted.pop(0)
        smallestK = kSorted[0]
        if smallestN > smallestK:
            moveN = (smallestN, "0.999999..")
        else:
            moveN = (smallestN, kSorted[-1]-0.000001)

        biggestK = kSorted[-1]
        if moveN[1] > biggestK:
            moveK = kSorted.pop(0)
        else:
            popK = 0
            breakLoop = False
            for x in range(len(kSorted)):
                if not breakLoop:
                    if kSorted[x] > moveN[1]:
                        popK = x
                        breakLoop = True
            moveK = kSorted.pop(popK)

        if moveN[0]>moveK: nCheatWins += 1
        # print "%s. N(%s|%s) %s K(%s)" %(r, moveN[0], moveN[1], {True: ">", False:"<"}[moveN[1]>moveK], moveK)
    return nCheatWins, nRealWins

for case in range(TestCases):
    solution = SolveProblem(lines[startLine:startLine+3])
    print >>outputFile, "Case #%s:" %(case+1), solution[0], solution[1]
    startLine += 3


outputFile.close()
print "DONE!"