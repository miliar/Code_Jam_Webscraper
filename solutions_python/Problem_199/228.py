#!/usr/bin/env python3

# pks is a boolean list
# flp is an integer
def flips(pks, flp):
    "return the number of flips needed"
    if flp < 1:
        return (0,-1)[False in pks]
    f = 0 # number of flip
    while pks:
        if not pks[0]:
            if len(pks) < flp:
                return -1
            for p in range(flp): # flip
                pks[p] ^= True
            f += 1
        pks.pop(0) # remove a "+"
    return f


import sys
file=sys.stdin

n = int(file.readline()) # number of cases
for i in range(1, n+1):
    pks, flp = file.readline().split()
    pks = [pk=='+' for pk in pks] # pankakes
    flp = int(flp) # flipper size

    f = flips(pks, flp)

    if f < 0: f = "IMPOSSIBLE"
    print("Case #%d: %s" % (i,f))
