
import sys

lines = open(sys.argv[1]).readlines()
nlines = len(lines)

T = int(lines[0])

casenum = 0

pos = 1

while pos < nlines:
    casenum = casenum+1

    vals = lines[pos].split()
    pos += 1
    D = int(vals[0])
    N = int(vals[1])

    T = []
    for i in xrange(N):
        vals = lines[pos].split()
        pos += 1
        K = int(vals[0])
        S = int(vals[1])
        T.append((0.0 + D - K) / S)
        
    print 'case #' + str(casenum) + ":", D / max(T)

    
