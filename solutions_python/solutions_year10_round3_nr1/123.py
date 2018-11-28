#
# Google Code Jam 2010
# Roaund 1C: A. Rope Intranet
# submission by EnTerr
#

import sys

f = open(sys.argv[1])
def input(): return f.readline().strip();



for caseNo in xrange(1, int(input())+1):
    wires = [map(int, input().split()) for i in range(int(input()))]
    n = 0
    for (x,y) in wires:
        for (a,b) in wires:
            if (x-a)*(y-b) < 0:
                n += 1    
    print 'Case #%d: %d' % (caseNo, n/2)

