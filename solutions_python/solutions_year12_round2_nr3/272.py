#
# Google Code Jam 2012
# Round 1B: C. Equal Sums
# submission by EnTerr
#

'''
Input
2
20 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
20 120 266 858 1243 1657 1771 2328 2490 2665 2894 3117 4210 4454 4943 5690 6170 7048 7125 9512 9600

Output
Case #1:
1 2
3
Case #2:
3117 4210 4943
2328 2894 7048

'''

#import psyco
#psyco.full()

import sys
from collections import defaultdict
#from time import clock

inf = open(sys.argv[1])
def input(): return inf.readline().strip()

def equalSums(lst):
    #res = None
    h = defaultdict(set)
    h[0] = set([frozenset([0])])
    for i in lst:
        for k in h.keys():
            h[i+k].update((s | frozenset([i])) for s in h[k])
            if len(h[i+k]) > 1:
                r = list(h[i+k])
                return list(r[0]-r[1]), list(r[1]-r[0])
            #except: print k,i,i+k, h[k], h; raise
    return None

for caseNo in range(1, int(input())+1):
    #print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo
    res = equalSums(sorted(map(int, input().split())[1:]))
    if res:
        print ' '.join(`i` for i in res[0])
        print ' '.join(`i` for i in res[1])
    else:
        print 'Impossible'

    
