#
# Google Code Jam 2010
# Roaund 1C: B. Load Testing
# submission by EnTerr
#

import sys
#import psyco
#psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();

def getNumTests(l, p, c):
    #print l,p,c
    if l*c >= p:
        return 0
    else:
        mid = (l*p) ** .5
        return 1+max(getNumTests(l, mid, c), getNumTests(mid, p, c))

for caseNo in xrange(1, int(input())+1):
    (L, P, C) = map(int, input().split())
    print 'Case #%d: %d' % (caseNo, getNumTests(L, P, C))

