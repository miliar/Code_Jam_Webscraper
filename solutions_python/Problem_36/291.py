# Problem from Google Code Jam 2009
import sys
import string

file = open(sys.argv[1])
numCases = int(file.readline())
welcome = "welcome to code jam"
for case in range(1, numCases+1):
    testStr = file.readline().strip()
    t = [[0 for j in range(len(testStr))] for i in range(len(welcome))]

    for i in range(len(welcome)):
        t[i][0] = 0
    t[0][0] = welcome[0] == testStr[0]

    for i in range(len(welcome)): # rows
        for j in range(1, len(testStr)): # cols
            if i==0:
                t[0][j] = t[0][j-1] + (welcome[i] == testStr[j])
            elif welcome[i] == testStr[j] :
                t[i][j] = t[i][j-1] + t[i-1][j]
            else:
                t[i][j] = t[i][j-1]
    print 'Case #%d: %s' % (case, string.zfill(str(t[len(welcome)-1][len(testStr)-1])[-4:],4))
