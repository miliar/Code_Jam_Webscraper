filename = "A-large.in"
outputname = filename + "out.txt"

inFile = open(filename, 'r')
outFile = open(outputname, 'w')

numCases = int(inFile.readline())

def sortByThird(walks):
    temp = [0,0,0]
    for i in range(len(walks)):
        for j in range(i, len(walks)):
            if walks[j][2] < walks[i][2]:
                temp[0] = walks[i][0]
                temp[1] = walks[i][1]
                temp[2] = walks[i][2]
                walks[i][0] = walks[j][0]
                walks[i][1] = walks[j][1]
                walks[i][2] = walks[j][2]
                walks[j][0] = temp[0]
                walks[j][1] = temp[1]
                walks[j][2] = temp[2]
    return walks

for i in range(numCases):
    nextLine = inFile.readline().split()
    corrLen = int(nextLine[0])
    walkingSpeed = int(nextLine[1])
    runningSpeed = int(nextLine[2])
    runningSeconds = int(nextLine[3])
    numWalkways = int(nextLine[4])
    
    walkways = [[0]*3 for j in range(numWalkways)]
    for j in range(numWalkways):
        nextLine = inFile.readline().split()
        walkways[j] = [int(nextLine[0]), int(nextLine[1]), int(nextLine[2])]

    walks = []
    walkwayIndex = 0
    endDist = 0
    while endDist < corrLen:
        if walkwayIndex < len(walkways) and walkways[walkwayIndex][0] == endDist:
            walks += [[walkways[walkwayIndex][0], walkways[walkwayIndex][1], walkingSpeed + walkways[walkwayIndex][2]]]
            endDist = walkways[walkwayIndex][1]
            walkwayIndex = walkwayIndex + 1
        elif walkwayIndex < len(walkways):
            walks += [[endDist, walkways[walkwayIndex][0], walkingSpeed]]
            endDist = walkways[walkwayIndex][0]
        else:
            walks += [[endDist, corrLen, walkingSpeed]]
            break

    sortedWalks = sortByThird(walks)
    manipulatedWalks = []
    while runningSeconds > 0:
        if len(sortedWalks) == 0:
            break
        nextWalk = sortedWalks.pop(0)
        newSpeed = nextWalk[2] + runningSpeed - walkingSpeed
        dist = nextWalk[1]-nextWalk[0]
        if dist*1.0/newSpeed < runningSeconds:
            runningSeconds -= dist*1.0/newSpeed
            manipulatedWalks += [[nextWalk[0], nextWalk[1], newSpeed]]
        else:
            distRun = newSpeed * runningSeconds
            manipulatedWalks += [[nextWalk[0], nextWalk[0] + distRun, newSpeed]]
            manipulatedWalks += [[nextWalk[0] + distRun, nextWalk[1], nextWalk[2]]]
            manipulatedWalks += sortedWalks
            break
    time = 0
    for j in range(len(manipulatedWalks)):
        time += ((manipulatedWalks[j][1]-manipulatedWalks[j][0])*1.0)/manipulatedWalks[j][2]

    print "Case #" + str(i+1) + ": " + str(time) + "\n"
    outFile.write("Case #" + str(i+1) + ": " + str(time) + "\n")        
    

inFile.close()
outFile.close()
