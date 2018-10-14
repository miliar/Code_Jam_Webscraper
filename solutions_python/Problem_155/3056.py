inputFileName = "A-large.in"
outputFileName = "Solutions.txt"
inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'w')
numCases = int(inputFile.readline())


def solve(s_max, s_dist):
    numFriends = 0
    standingAudience = 0
    for i in range(s_max+1):
        if standingAudience < i:
            numFriends += 1
            standingAudience += 1
        standingAudience += int(s_dist[i])
    return numFriends




for i in range(numCases):
    currentLine = inputFile.readline().split()
    s_max = int(currentLine[0])
    s_dist = currentLine[1]
    outputFile.write("Case #%s: %s\n"%(i+1, solve(s_max, s_dist)))