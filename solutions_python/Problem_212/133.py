#!/usr/bin/env python3

# !py a.py < a.in > a.out



def main():
    t = int(input())
    for i in range(1, t+1):
        #input
        n, p = map(int, input().split())
        g = list(map(int, input().split()))
        
        #comput
        ans = solve(p, g)
        
        
        #output
        print('Case #%d:' % i, ans)
    


def solve(p, g):
    groups = Counter(size % p for size in g)
    if p == 2:
        return groups[0] + (groups[1] + 1)//2
    elif p == 3:
        total = groups[0]
        total += min(groups[1], groups[2])
        if groups[1] == groups[2]:
            pass
        elif groups[1] > groups[2]:
            total += (groups[1] - groups[2] + 2)//3
        else:
            total += (groups[2] - groups[1] + 2)//3
    elif p == 4:
        total = groups[0]
        total += (groups[2] + 1)//2
        total += min(groups[1], groups[3])
        if groups[1] == groups[3]:
            return total
        elif groups[1] > groups[3]:
            leftover = groups[1] - groups[3]
        else:
            leftover = groups[3] - groups[1]
        if groups[2] % 2:
            leftover -= 2
        if leftover > 0:
            total += (leftover + 3)//4
    return total




###################


from sys import stdin, stdout, stderr
import operator as op
from functools import *
memoize = lru_cache(None)
from itertools import *
from collections import *
chainit = chain.from_iterable
flatten = chain.from_iterable


iget = op.itemgetter

get0 = iget(0)
get1 = iget(1)
get2 = iget(2)





###############

main()

