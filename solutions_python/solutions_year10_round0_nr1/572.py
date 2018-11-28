def CalculateFinalState(numClappers, numIterations):
    allOn = "OFF"
    allOnState = (2**numClappers)-1
    if numIterations > allOnState:
        if numClappers == 1:
            if numIterations % 2 == 1:
                allOn = "ON"
        elif (numIterations + 1) % (allOnState + 1) == 0:
            allOn = "ON"
    elif allOnState == numIterations:
            allOn = "ON"
    return allOn

inFile = open('Sol1.in')
outFile = open('Sol1.out','w')
numCases = int(inFile.readline())
for x in range(numCases):
    caseLine = inFile.readline()
    caseLine = caseLine.split()
    outFile.write("Case #" + str(x + 1) + ": " + CalculateFinalState(int(caseLine[0]), int(caseLine[1])) + "\n")
inFile.close()
outFile.close()