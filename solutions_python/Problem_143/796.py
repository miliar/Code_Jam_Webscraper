import sys
line = sys.stdin.readline()
numTests = int(line)
for test in xrange(1, numTests+1):
    inp = sys.stdin.readline().split(' ')
    A = int(inp[0])
    B = int(inp[1])
    K = int(inp[2])
    ways = 0

    for a in xrange(0, A):
        for b in xrange(0, B):
                if (a & b) < K:
                    ways += 1
    print 'Case #%d: %d' %(test, ways)            
