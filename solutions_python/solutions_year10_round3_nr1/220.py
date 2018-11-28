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
     
    N = int(caseline1)
    
    buildHeight = []
    for i in range(N):
        caseline2 = inputfile.readline().replace("\n", "")
        #(A,B) = map(int, caseline1.split(" "))
        buildHeight.append(map(int, caseline2.split(" ")))
    
    crossed = 0
    for i in range(N):
        (A,B)=  buildHeight[i]
        for (j,k) in enumerate(buildHeight):
            if j > i:
                continue
            (At, Bt) = k
            if (A - At) * (B - Bt) < 0:
                crossed += 1
        
    print >> outputfile, "Case #%d: %d" % (caseNo+1, crossed)
    caseNo += 1
inputfile.close()
outputfile.close()