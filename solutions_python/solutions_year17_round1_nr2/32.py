#!/usr/bin/env python3

# !py a.py < a.in > a.out



def main():
    t = int(input())
    for i in range(1, t+1):
        #input
        n, p = map(int, input().split())
        rs = list(map(int, input().split()))
        qs = [list(map(int, input().split())) for _ in range(n)]
        
        #comput
        ans = solve(rs, qs)
        
        
        #output
        print('Case #%d:' % i, ans)
    


#rs[i]: grams of the i'th ingredient.
#qs[i][j]: i'th ingredient, j'th package.
def solve(rs, qs):
    for q in qs:
        q.sort(reverse=True)

    # Merge: Try to take the smallest remaining packages.
    # If it can't be in a kit, discard the relatively-smallest package.
    kits = 0
    while all(qs):
        ps = [q[-1] for q in qs]
        ranges = [serving_range(r, p) for r,p in zip(rs, ps)]
        print("ranges:", ranges, file=stderr)
        servings = reduce(merge_ranges, ranges)
        if servings:
            kits += 1
            print("kit:", ps, file=stderr)
            for q in qs:
                q.pop()
        else:
            cap = min(rg.stop for rg in ranges)
            for i, (rg, q) in enumerate(zip(ranges, qs)):
                if rg.stop == cap:
                    print("popping:", i, q[-1], file=stderr)
                    q.pop()
    return kits


def merge_ranges(r0, r1):
    return range(max(r0.start, r1.start), min(r0.stop, r1.stop))


def serving_range(r, p):
    serving_min = ceildiv(p*10, 11*r)
    serving_max = p*10 // (9*r)
    return range(serving_min, serving_max+1)


def ceildiv(n, d):
    return (n + d - 1) // d




###################


from sys import stdin, stdout, stderr
import operator as op
import math
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

