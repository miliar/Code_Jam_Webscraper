#
# Google Code Jam 2015
# Roaund 0: C. Dijkstra
# submission by EnTerr
#

'''

Input 
 
5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i

Output 

Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO

'''



import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

from math import copysign

i, j, k = 2, 3, 4
tab = { }
tab[1,1] = 1
tab[i,1] = tab[1,i] = i
tab[j,1] = tab[1,j] = j
tab[k,1] = tab[1,k] = k
tab[i,i] = -1
tab[i,j] = k;   tab[j,i] = -k
tab[i,k] = -j;  tab[k,i] = j
tab[j,j] = -1
tab[j,k] = i;   tab[k,j] = -i
tab[k,k] = -1
for x in [-1, -i, -j, -k, 1, i, j, k]:
    for y in [-1, -i, -j, -k, 1, i, j, k]:
        if (x,y) not in tab:
            tab[x,y] = tab[abs(x),abs(y)] * copysign(1, x) * copysign(1, y)

#detab = {1: '1', 2: 'i', 3:'j', 4:'k'}
       
def is_ijk(q_list, i=i, j=j, k=k, tab=tab):
    #print '---', q_list
    it = iter(q_list)
    try:
        for goal in [i, j, k]:
            r = 1
            while r <> goal:
                # keep multiplying till you get it
                n = it.next()
                #print r, n, 
                r = tab[r, n]
                #print r
    except StopIteration: return False
    
    try: # exhaust the tail, result should be 1
        r = 1
        while True:
            r = tab[r, it.next()]
    except StopIteration: 
        return r == 1

#clk = clock()

for caseNo in xrange(1, int(input())+1):
    l, x = map(int, input().split())
    dec = {'i': i, 'j': j, 'k': k}
    q_str = [dec[c] for c in input()]
#    print >>sys.stderr, caseNo
    print 'Case #%d:' % caseNo, 'YES' if is_ijk(q_str * x) else 'NO'
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

