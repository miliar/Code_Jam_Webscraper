import sys

inp = sys.stdin

T = int(inp.readline())

for testCase in xrange(1, T+1):
    
    l = inp.readline().split(" ")
    
    n = int(l[0])
    m = int(l[1])

    nLinesMax = [0]*n
    mLinesMax = [0]*m

    lawn = [[0]*m for i in xrange(n)]

    for i in xrange(n):
        l = map(lambda x: int(x), inp.readline().split(" "))
        for j in xrange(m):
            newHeight = l[j]
            nLinesMax[i] = max(newHeight, nLinesMax[i])
            mLinesMax[j] = max(newHeight, mLinesMax[j])
            lawn[i][j] = newHeight
    

    state = 1
    
    for i in xrange(n):
        for j in xrange(m):
            h = lawn[i][j]
            if h < nLinesMax[i] and h < mLinesMax[j]:
                state = 0
                break
        if state == 0:
            break

    stateDescription = ""

    if state:
        stateDescription = "YES"
    else:
        stateDescription = "NO"
        
    print "Case #{}: {}".format(testCase, stateDescription)


