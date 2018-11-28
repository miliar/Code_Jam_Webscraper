import sys
import array
import fractions
from heapq import heappush, heappop

T = int(input())
for t in range(1,T+1):
    N,PD,PG=map(int,input().split())
    p='Possible'
    if PG == 100:
        if PD != 100:
            p='Broken'
    elif PG == 0:
        if PD != 0:
            p='Broken'
    elif PD == 0:
        pass
    else:
        g=fractions.gcd(100,PD)
        #print(100//g)
        if 100//g > N:
            p='Broken'
    print('Case #{0}:'.format(t), p)
