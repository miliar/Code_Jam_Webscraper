
def parseInput(fileName):
    """
    Read a file and return the persons at each shy level as a list
    """
    f = open(fileName, 'r')
    fileContent = f.read()
    allLines = fileContent.split("\n")
    numTestCases = allLines[0]
    testCases = allLines[1:]
    
    shyness = list()
    for tc in testCases:
        maxShyAndEachShy = tc.split(" ")
        if(len(maxShyAndEachShy) == 2):
            maxShy = maxShyAndEachShy[0]
            eachShy = maxShyAndEachShy[1]
            # Number of persons in each shyness level
            shyCaps = map(int, list(eachShy))
            shyness.append(shyCaps)
    
    f.close()
    return (shyness)
    
def writeOut(inFile, outFile):    
    shyness = parseInput(inFile)
    numTestCases = len(shyness)
    
    f = open(outFile, 'w')
    count = 1
    for tc in shyness:
        lenShy = len (tc)
        shyLevels = range(lenShy)
        standers = 0
        totalIntruders = 0
        
        for shyLevel in shyLevels:
            intruders = (shyLevel - standers) if (shyLevel > standers) else 0
            standers = standers + intruders + tc[shyLevel]
            totalIntruders = totalIntruders + intruders
        
        outLine = "Case #" + str(count) + ": " + str(totalIntruders) + "\n"
        f.write(outLine)
        count = count + 1
    f.close()
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print "Usage: standingOvation.py inFile outFile"
        sys.exit(1)
        
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    
    writeOut(inFile, outFile)
    