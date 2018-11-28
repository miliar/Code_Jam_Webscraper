#!/usr/bin/env python
# encoding: utf-8
"""
SpaceEmergency.py

Created by Graham Dennis on 2011-05-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys

# def permutations(*iterables):
#     def permuteTwo(it1, it2):
#         for o1 in it1:
#             for o2 in it2:
#                 if isinstance(o1, tuple):
#                     yield o1 + (o2,)
#                 else:
#                     yield (o1, o2)
# 
#     if len(iterables) == 1:
#         return iterables[0]
# 
#     it = iterables[0]
#     for it2 in iterables[1:]:
#         it = permuteTwo(it, it2)
# 
#     return it
# 
# def combinations(itemCount, *lsts):
#     """Generator for all unique combinations of each list in `lsts` containing `itemCount` elements."""
#     def _combinations(itemCount, lst):
#         if itemCount == 0 or itemCount > len(lst):
#             return
#         if itemCount == 1:
#             for o in lst:
#                 yield (o,)
#         elif itemCount == len(lst):
#             yield tuple(lst)
#         else:
#             if not isinstance(lst, list):
#               lst = list(lst)
#             for o in _combinations(itemCount-1, lst[1:]):
#                 yield (lst[0],) + o
#             for o in _combinations(itemCount, lst[1:]):
#                 yield o
#     if len(lsts) == 1:
#         return _combinations(itemCount, lsts[0])
#     iterables = [list(_combinations(itemCount, lst)) for lst in lsts]
#     return permutations(*iterables)


def combinations(N, items):
    if N == 0:
        pass
    elif N == 1:
        for i in items:
            yield (i,)
    elif N == 2:
        for i in xrange(len(items)):
            for j in xrange(i):
                yield (items[j], items[i])

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for case in xrange(T):
        integers = map(int, f.readline().split())
        L, t, N, C = integers[:4]
        distancePattern = integers[4:]
        distances = distancePattern * ((N/C) + 1)
        times = [2 * sum(distances[:N])]
        validBoosterLocations = []
        currentTime = 0
        for i in xrange(N):
            currentTime += 2 * distances[i]
            if currentTime > t:
                validBoosterLocations.append(i)
        if len(validBoosterLocations) < L:
            L = len(validBoosterLocations)
        # print validBoosterLocations
        for boosterPattern in combinations(L, validBoosterLocations):
            currentTime = 0
            for i in xrange(N):
                if not i in boosterPattern:
                    currentTime += 2 * distances[i]
                elif currentTime >= t:
                    currentTime += distances[i]
                elif currentTime + 2 * distances[i] <= t:
                    currentTime += 2 * distances[i]
                else:
                    remainingDistance = distances[i] - (t - currentTime)/2
                    currentTime = t + remainingDistance
            times.append(currentTime)
        
        print "Case #%i: %i" % (case + 1, min(times))

if __name__ == "__main__":
    sys.exit(main())
