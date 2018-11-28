INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())

for t in range(T):
    N, M = [int(i) for i in f_in.readline().split()]
    mkdirNum = 0
    folderTree = []
    for n in range(N):
        # cut of root slash
        folderTree.append(f_in.readline().strip()[1:])
    for m in range(M):
        # subdir is going after parent dir
        folderTree.sort()        
        
        newFolder = f_in.readline().strip()[1:]
        closestParent = ''
        for folder in folderTree:
            if newFolder.startswith(folder):
                closestParent = folder
                
        currentPos = len(closestParent) + 1
        while currentPos <= len(newFolder):
            nextSep = newFolder.find('/', currentPos)
            if nextSep == -1:
                nextSep = len(newFolder)
            folderTree.append(newFolder[0:nextSep])
            mkdirNum += 1
            currentPos = nextSep + 1
        
    strRes = "Case #" + str(t + 1) + ": " + str(mkdirNum)
    f_out.write(strRes + "\n")
    print(strRes) 

f_in.close()
f_out.close()
