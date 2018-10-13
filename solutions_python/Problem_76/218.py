#
# Google Code Jam 2011
# Roaund 0: C. Candy Splitting
# submission by EnTerr
#

'''
Input 
2
5
1 2 3 4 5
3
3 5 6
 	
Output 
Case #1: NO
Case #2: 11
'''

import sys
#import psyco
#psyco.full()

f = open(sys.argv[1])
def input(): return f.readline().strip();


def splitCandies(seq):
    s = 0
    for i in seq:
        s ^= i

    if s == 0:
        return sum(seq)-min(seq)
    else:
        return 'NO'


for caseNo in range(1, int(input())+1):
    input() # skip line
    print 'Case #%d:' % caseNo, splitCandies( map(int, input().split()) )

