from __future__ import print_function
import sys

# print to stderr for debugging
enableDebug = True
def printe(*stuff):
    if enableDebug:
        print(*stuff, file=sys.stderr) 


# Open file for processing
filename = sys.argv[1]
inputFile = open(filename, 'r')
lines = [l.rstrip('\n') for l in inputFile]
linesIter = iter(lines)
nCases = int(linesIter.next())



# Process each case
for iCase in range(1,nCases+1):
    # printe("\nProcessing case " + str(iCase))

    # Solve problem
    items = linesIter.next().split(' ')
    nGroups = int(items[0])
    nPack = int(items[1])

    groups = [int(x) for x in linesIter.next().split(' ')]

    groupCounts = [0] * (nPack)
    for g in groups:
        groupCounts[g % nPack] += 1

    if nPack == 2:
        packSets = [
           (1,0),
           (0,2)
        ]
    elif nPack == 3:
        packSets = [
           (1,0,0),
           (0,1,1),
           (0,3,0),
           (0,0,3),
        ]
    elif nPack == 4:
        packSets = [
           (1,0,0,0),
           (0,1,0,1),
           (0,0,2,0),
           (0,2,1,0),
           (0,0,1,2),
           (0,4,0,0),
           (0,0,0,4),
        ]


    nFresh = 1

    for packSet in packSets:

        while True:

            canBuild = True
            for i in range(nPack):
                if not groupCounts[i] >= packSet[i]:
                    canBuild = False

            if not canBuild:
                break

            nFresh += 1
            for i in range(nPack):
                groupCounts[i] -= packSet[i]


    sumGroup = 0
    for i in range(nPack):
        sumGroup += groupCounts[i]

    if(sumGroup == 0): nFresh -= 1


    print("Case #{}: {}".format(iCase, nFresh))
