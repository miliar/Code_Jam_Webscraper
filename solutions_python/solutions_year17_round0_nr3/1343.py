import sys
from heapq import *
sys.stdin  = open('input.in', 'r')
sys.stdout = open('output.txt', 'w')

for _ in xrange(1,input()+1):
    print 'Case #' + str(_) + ':',
    n, k = map(int,raw_input().split())
    a = []
    heappush(a,-n)
    l,r = n,n
    for i in xrange(k):
        j = abs(heappop(a))
        if j%2 == 0:
            l,r = j/2-1,j/2
            heappush(a,-l);heappush(a,-r)
        else:
            l,r = j/2,j/2
            heappush(a,-l);heappush(a,-r)
        if j <= 0 : break
    print r,l