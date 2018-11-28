from math import sqrt, pow, log, ceil, log10, floor
from sys import stdin, setrecursionlimit
import copy
import random

setrecursionlimit(100000)
debug = 0

def solve(N, array):

    # 0 or 1 hiker: return 0
    nb = 0
    for i in range(N):
        (d, h, m) = array[i]
        nb += h

    if nb <= 1:
        if debug:
            print "h <= 1"

        return 0

    # case h == 2: the idea is to go just before the closer, then follow him, and not being
    # touched by the further. So, is it possible? If yes, return 0. If not, try to be touched 
    # just once. If really not possible, say 2 (infinite speed)

    if N == 1:
        # group of 2
        (d0, h, m0) = array[0]
        (d1, m1) = (d0, m0 + 1)
    else:
        # two groups
        (d0, h, m0) = array[0]
        (d1, h, m1) = array[1]

    # same speed?
    if m0 == m1:
        if debug:
            print "m0 == m1"
        return 0

    # Not same speed

    # let say d0 is the closer one
    if d1 < d0:
        (a, b) = (d0, m0)
        (d0, m0) = (d1, m1)
        (d1, m1) = (a, b)

    # now d0 is smaller (or equal) than d1

    if debug:
        print "(d0, m0)", (d0, m0)
        print "(d1, m1)", (d1, m1)

    # we go to d0

    # if d0 is slower:
    if m0 >= m1:

        # if d0 will have finished the round before d1 has finished two rounds, that's 0
        # if m0 * (360 - d0) / 360 < m1 * (720 - d1) / 360:
        if m0 * (360 - d0) < m1 * (720 - d1) :
            if debug:
                print "aaa"
            return 0

        # else we skip over d0 then follow d1
        return 1

    # if d0 is faster

    # if d1 will have finished the round before d0 has finished two rounds, that's 1
    # if m1 * (360 - d1) / 360 < m0 * (720 - d0) / 360:
    if m1 * (360 - d1) < m0 * (720 - d0) :
        if debug:
            print "ddd"
        return 0

    if debug:
        print "eee"

    return 1

T = int(stdin.readline())

for mii in range(1,T+1):
    
    N, = map(int, stdin.readline().split(' '))
    array = []
    for i in range(N):
        D, H, M = map(int, stdin.readline().split(' '))
        array.append((D, H, M))

    print "Case #" + str(mii) + ":", 

    if debug:
        print
        print N
        print array

    rep = solve(N, array)

    print rep
