import fractions
import math
def casePrint(i, result):
    writer.write('Case #'+str(i)+': '+result+'\n')




inputFile = 'd:/C-small.in'
outputFile = 'd:/C-small.out'
reader = open(inputFile, 'r')
writer = open(outputFile, 'w')

numCases = int(reader.readline())

for i in range(1, numCases+1):
    [runTimes, capacity, numGroups]  = reader.readline().strip().split(' ')
    runTimes = int(runTimes)
    capacity = int(capacity)
    numGroups = int(numGroups)
    groups = reader.readline().strip().split(' ')
    for j in range(0, numGroups):
        groups[j] = int(groups[j])

    totalPerson = 0;
    while runTimes > 0:
        personLeft = capacity
        onBoardGroups = 0
        while 1:
            nextGroup = groups[0]
            if personLeft - nextGroup >= 0 and onBoardGroups < len(groups):
                personLeft -= nextGroup
                totalPerson += nextGroup
                groups = groups[1:]
                groups.append(nextGroup)
                onBoardGroups += 1
            else:
                break
        runTimes -= 1
    casePrint(i, str(totalPerson))
                


reader.close();
writer.close();
