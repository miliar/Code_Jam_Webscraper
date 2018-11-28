import sys
from itertools import *

T = int(sys.stdin.readline())

for t in range(T):
    
    R, k, N = [int(num) for num in sys.stdin.readline().split()]
    G = [int(num) for num in sys.stdin.readline().split()]

    passangers = 0
    money = 0
    n = 0
    
    #print R, k, N
    #print G
    for group in cycle(G):
       # print R, passangers, group, n
        if (passangers + group <= k) and (n < N):
            passangers += group
            n += 1
        elif R > 0:
        #    print '\t',passangers
            money += passangers
            passangers = group
            n = 1
            R -= 1
        else:
            break

    print 'Case #{0}: {1}'.format(t+1, money)
