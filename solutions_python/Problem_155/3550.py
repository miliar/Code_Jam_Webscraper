file = open("A-small-attempt1.in", "r")
numCases = int(file.readline())

for i in range(0, numCases):
    strCase = file.readline()
    maxShy = int(strCase[0])

    numPeepsArr = []

    for i2 in range(0, maxShy + 1):
        numPeepsArr.append(strCase[2 + i2])

    clappers = 0
    friends = 0
    for shyness in range(0, maxShy+1):
        while (shyness > clappers):
            friends += 1
            clappers += 1
        clappers += int(numPeepsArr[shyness])

    print "Case #" + str(i+1) + ": " + str(friends)
