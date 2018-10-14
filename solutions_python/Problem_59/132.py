
FILE = open("A-large.in","r")
OUTPUT = open("A-large.out","w")

cases = FILE.readline()

for i in range(0,int(cases)):
    temp = FILE.readline().split(" ")
    n = int(temp[0])
    m = int(temp[1])
    existingDirs = []
    dirsToCreate = []
    for j in range(0,n):
        existingDirs.append(FILE.readline().rstrip('\n'))
    for k in range(0,m):
        dirLine = FILE.readline().rstrip('\n')
        if not dirLine in existingDirs:
            dirsToCreate.append(dirLine)
    folderStructure = {}
    for line in existingDirs:
        folderList  = line.split('/')[1:]
        currentDir = folderStructure
        for folderName in folderList:
            if not folderName in currentDir:
                currentDir[folderName] = {}
            currentDir = currentDir.get(folderName)
    count = 0
    for line in dirsToCreate:
        folderList  = line.split('/')[1:]
        currentDir = folderStructure
        for folderName in folderList:
            if not folderName in currentDir:
                currentDir[folderName] = {}
                count += 1
            currentDir = currentDir.get(folderName)
    OUTPUT.write("Case #" + str(i+1) + ": " + str(count) + "\n")
    print count
        

FILE.close()
OUTPUT.close()

