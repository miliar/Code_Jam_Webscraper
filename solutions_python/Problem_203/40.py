#!/usr/bin/env python3

# !py a.py < a.in > a.out



def main():
    t = int(input())
    for i in range(1, t+1):
        #input
        r, c = map(int, input().split())
        cake = [list(input()) for _ in range(r)]
        
        #comput
        ans = solve(cake)
        
        
        #output
        print('Case #%d:' % i)
        for line in ans:
            print(*line, sep='')


def solve(cake):
    """cake: list[list[C]]
    where c is uppercase English, or question mark
    """
    kids = set(flatten(cake))
    if '?' not in kids:
        return cake
    kids -= {'?'}
    
    def find(kid):
        for i, row in enumerate(cake):
            try:
                return i, row.index(kid)
            except ValueError:
                pass
            
    
    #? Does greedy work?
    for kid in kids:
        i, j = find(kid)
        #expand vertically
        ilo, ihi = i, i+1
        while ilo > 0 and cake[ilo-1][j] == '?':
            ilo -= 1
        while ihi < len(cake) and cake[ihi][j] == '?':
            ihi += 1
        jlo, jhi = j, j+1
        while jlo > 0 and all(cake[x][jlo-1] == '?' for x in range(ilo, ihi)):
            jlo -= 1
        while jhi < len(cake[i]) and all(cake[x][jhi] == '?' for x in range(ilo, ihi)):
            jhi += 1
        for i in range(ilo, ihi):
            for j in range(jlo, jhi):
                cake[i][j] = kid
    return cake


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

