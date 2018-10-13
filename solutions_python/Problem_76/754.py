import sys
from itertools import chain, combinations
from operator import xor

cin = sys.stdin
cin.next() # skip line saying number of cases


def powerset(s): # except for the full set of s
    return chain.from_iterable(combinations(s, r) for r in range(len(s)))


case = 0
useless = False
for line in cin:
    useless = not useless
    if not useless:
        case += 1
        candies = map(int, line.strip().split(' '))
        all_xor = reduce(xor, candies)

        best = None

        for seans in powerset(candies):
            sean_value = sum(seans)
            seans_xor = reduce(xor, seans) if len(seans) else 0
            patrick_value = xor(all_xor, seans_xor)
            if seans_xor  == patrick_value and (best is None or sean_value > best):
                best = sean_value

        if best is None:
            print("Case #%d: NO" % (case,))
        else:
            print("Case #%d: %d" % (case, best))



