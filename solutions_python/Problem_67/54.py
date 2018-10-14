#
# Google Code Jam 2010
# Roaund 2: C. Bacteria
# submission by EnTerr
#

import sys
from time import clock

import psyco
psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();

def doBoard():
    s = set()
    for i in range(int(input())):
        x1,y1,x2,y2 = map(int, input().split())
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                s.add( (i,j) )
    ticks = 0
    while s:
        # print s
        ticks += 1
        s1 = set()
        for i,j in s:    
            if (i-1,j) in s or (i, j-1) in s:
                s1.add( (i,j) )     # lives
            if (i-1,j+1) in s:
                s1.add( (i,j+1) )   # born
        s = s1
    print ticks
        

clk = clock()
for caseNo in xrange(1, int(input())+1):
    print 'Case #%d:' % caseNo,
    doBoard()
print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

