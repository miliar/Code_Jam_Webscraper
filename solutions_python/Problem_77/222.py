#
# Google Code Jam 2011
# Roaund 0: D. Goro Sort
# submission by EnTerr
#

'''
Input 
3
2
2 1
3
1 3 2
4
2 1 4 3
 	
Output 
Case #1: 2.000000
Case #2: 2.000000
Case #3: 4.000000
'''

import sys
#import psyco
#psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();

def fact(x):
    return reduce(lambda x,y:x*y, range(1,x+1)) 

def goroSort(seq):
    seq.insert(0,0) # python arrays start from 0, we want them from 1
    visited = set()
    res = 0
    for i in range(1,len(seq)):
        # found all cycles >1 
        j = i; n = 0
        while j not in visited:
            visited.add(j)
            j = seq[j]
            n += 1
        if n>1:
            # res += 2*(n-1)
            res += n

    return res


for caseNo in range(1, int(input())+1):
    input() # skip line
    print >>sys.stderr, caseNo
    print 'Case #%d: %f' % (caseNo, goroSort( map(int, input().split()) ))

