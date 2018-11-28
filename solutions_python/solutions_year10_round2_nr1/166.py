'''
Google Code Jam 2010
Created by : KenKen
Created on : 2010/05/23
'''

inputfile = open('A-large.in', 'r')
outputfile = open('output.txt', 'w')

T = inputfile.readline().replace("\n", "")   # Read the first line
T = int(T)

caseNo = 0
while caseNo < T:
    caseline1 = inputfile.readline().replace("\n", "")
    if not caseline1:
        break
     
    (N,M) = map(int, caseline1.split(" "))
    
    i = 0
    exPath = []
    while i < N: 
        exPath.append(inputfile.readline().replace("\n", ""))
        i += 1
    #print "exist:", exPath
    
    i = 0
    #wantPath = []
    #wantPath = []
    mkdirNo = 0
    while i < M: 
        wantPath = inputfile.readline().replace("\n", "")
        wantDirList = wantPath.split("/")[1:]
        #print "want:", wantDirList
    
        subPath = ""
        for dir in wantDirList:
            if not subPath:
                subPath = "/" + dir
            else:
                subPath += "/" + dir
            if subPath in exPath:
                pass
            else:
                mkdirNo += 1
                exPath.append(subPath)
                #print subPath
        
        i += 1  
    #print >> outputfile, "Case #%d: %d" % (caseNo+1, 1)
    print >> outputfile, "Case #%d: %d" % (caseNo+1, mkdirNo)
    caseNo += 1
    

inputfile.close()
outputfile.close()