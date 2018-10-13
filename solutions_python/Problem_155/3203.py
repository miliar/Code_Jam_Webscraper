
inputFile = open('A-large.in', 'r')
outputFile = open('output', 'w')

numTestCases = int(inputFile.readline())

for x in range(0, numTestCases):
    caseLine = inputFile.readline().split()
    maxShyness = int(caseLine[0])
    audienceShyness = list(caseLine[1])
    audienceShyness = map(int, audienceShyness)
    audienceCount = sum(audienceShyness)
    standingCount = 0
    addedFriends = 0

    while standingCount != audienceCount:
        standingCount = 0
        for j in range(len(audienceShyness)):
            if standingCount >= j:
                standingCount += audienceShyness[j]
        if standingCount != audienceCount:
            audienceShyness[0] += 1
            addedFriends += 1
            audienceCount += 1

    outputFile.write("Case #{0}: {1}\n".format(x+1, addedFriends))





