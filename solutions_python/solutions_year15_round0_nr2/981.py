#!/usr/bin/env python
from collections import Counter
from copy import copy
import sys

if len(sys.argv) != 2:
    print 'Usage: python shit.py <input file>'

with open(sys.argv[1]) as f:
    text = map(lambda x: x.strip(), f.readlines())
    numTestcases = int(text[0])
    testcases = zip(
        (int(z) for z in text[1::2]),
        ([int(z) for z in x.split()] for x in text[2::2]))

# for some reason, collections.Counter isn't hashable.
# disclaimer: this class is not safe at all for mutations
class HCounter(Counter):
    def __hash__(self):
        return hash(frozenset(self))
    def alts(self):
        key = max(self)
        for delta in range(1, key):
            alt = copy(self)
            if alt[key] > 1:
                alt[key] -= 1
            else:
                del alt[key]
            alt[key-delta] += 1
            alt[delta] += 1
            yield alt



# memoize all the things
memo = {}
def diningTime(pset_):
    pset = copy(pset_)  
    if pset not in memo:
        naive = max(pset)
        if naive <= 2:
            memo[pset] = naive
        else:
            memo[pset] = min(naive,1+min(diningTime(z) for z in pset.alts()))
    return memo[pset]


tc = 1
for (d, plist) in testcases:
    print 'Case #'+str(tc)+': '+str(diningTime(HCounter(plist)))
    tc += 1

