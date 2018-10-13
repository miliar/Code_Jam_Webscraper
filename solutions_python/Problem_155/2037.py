__author__ = 'neigh_000'

inFile = open("large.in")
outFile = open("large_out.txt", "w")

numCases = int(inFile.readline())

for case in range(numCases):
    maxShyness, shynessLevels = inFile.readline().split(" ")
    maxShyness = int(maxShyness)

    # necessary? maybe helpful
    shyDict = {}
    for shynessLevel in range(maxShyness+1):
        shyDict[shynessLevel] = int(shynessLevels[shynessLevel])

    numFriendsNeeded = 0
    standing = 0
    for i in range(maxShyness+1):
        standing += shyDict[i]
        if standing < i+1:
            # not enough people standing for next group to get up
            friendsAdded = i + 1 - standing
            numFriendsNeeded += friendsAdded
            standing += friendsAdded

    result = "Case #%s: %s\n" % (case+1, numFriendsNeeded)
    outFile.write(result)

inFile.close()
outFile.close()