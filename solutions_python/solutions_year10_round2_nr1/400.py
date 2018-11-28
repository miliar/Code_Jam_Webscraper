#split at /
#for each level, check if level exists
#    if not, create level

def BuildDirTable(hashtable, existingLines, value):
    for x in existingLines:
        dirs = x.split('/')
        dirs = dirs[1:]
        currentPath = ""
        for y in dirs:
            currentPath = currentPath + "/" + y
            if currentPath in hashtable:
                pass
            else:
                hashtable[currentPath] = value
            pass
    print(hashtable)

def SolveDIRs(numExistingLines, numNewLines, existingLines, newLines):
    hashtable = {}
    #add the existing dir's
    BuildDirTable(hashtable, existingLines, 0)
    BuildDirTable(hashtable, newLines, 1)
    numMKDirCmds = 0
    for x in hashtable.values():
        if x == 1:
            numMKDirCmds = numMKDirCmds + 1
    return str(numMKDirCmds)

inFile = open('A-large.in')
outFile = open('A-large.out','w')
numCases = int(inFile.readline())
for x in range(numCases):
    caseLine = inFile.readline()
    caseLine1 = caseLine.split()
    numExistingDirLines = int(caseLine1[0])
    numNewDirLines = int(caseLine1[1])
    existingDirs = []
    newDirs = []
    for y in range(numExistingDirLines):
        existingDirs.append((inFile.readline())[:-1])
    for y in range(numNewDirLines):
        newDirs.append((inFile.readline())[:-1])
    print("Case #" + str(x + 1) + ": numExisting=" + str(numExistingDirLines) + ", numNew=" + str(numNewDirLines))
    outFile.write("Case #" + str(x + 1) + ": " + SolveDIRs(numExistingDirLines, numNewDirLines, existingDirs, newDirs) + "\n")
inFile.close()
outFile.close()