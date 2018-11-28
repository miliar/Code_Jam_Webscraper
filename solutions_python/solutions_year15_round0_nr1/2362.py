numIteration = raw_input ()
for test in range(1, int(numIteration)+1):
    audience = raw_input ()
    maxShynessIndex =  int(audience.split(" ")[0])
    shynessInfo = audience.split(" ")[1]
    numStanding = 0
    numFriends = 0
    for shynessIndex in range(0, len(audience.split(" ")[1])):
        while numStanding < shynessIndex:
            numStanding += 1
            numFriends += 1
            if shynessIndex <= numStanding:
                break
        if numStanding >= shynessIndex:
            numStanding+= int(shynessInfo[shynessIndex])

    print "Case #" + str(test) + ": " + str(numFriends)