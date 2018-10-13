import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    param = sys.stdin.readline()
    param = param.split(' ')
    r = int(param[0])
    t = int(param[1])
    numRings = 0
    while(1):
        paintRequired = 2*r + 1
        if(paintRequired <= t):
            numRings = numRings + 1
            t = t - paintRequired
        else:
            break
        r = r + 2
    print 'Case #%d: %d' %(test,numRings)     
