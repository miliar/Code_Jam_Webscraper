#!/usr/bin/python

import sys


# If we ever remove a mote, it should be the largest one. But we
# might as well postpone removing motes to the end; that is, we first
# create whatever "stepping stones" he will need to consume some
# number of motes - if at some point the number of stepping stones we
# would need to add to consume the smallest remaining mote exceeds
# the number of remaining motes, we might as well remove all
# remaining motes.

def compute_motes_to_add(Armin, smallest):
    if Armin == 1: # nothing we can do, return a very very large number (well, just larger than the largest possible list size)
        return Armin, 100000000
    # We can make Armin -> 2*Armin-1 -> 4*Armin-3 -> 8*Armin-7 ->
    # ... This grows exponentially, so requires at most log2(10^6) ~=
    # 20 steps - no need to try to find some closed formula
    steps = 0
    while Armin <= smallest:
        Armin += Armin-1
        steps += 1
    return Armin, steps


def do_case(n):
    A,N = inp.readline().strip().split()
    A=int(A)
    N=int(N)
    ops = 0
    motes = [int(x) for x in inp.readline().strip().split()]
    assert N == len(motes)
    motes.sort()

    while (len(motes) > 0):
        newsize, motes_to_add = compute_motes_to_add(A, motes[0])
        if motes_to_add >= len(motes):
            ops += len(motes)
            motes = []
        else:
            ops += motes_to_add
            A = newsize
            # Since motes is sorted, this could be done more
            # efficiently, but the length is less than 100, so no need
            to_eat = [m for m in motes if m < A]
            remaining = [m for m in motes if m >= A]
            A += sum(to_eat)
            motes = remaining

    ops = min(ops, N)
    print "Case #%d: %d" % (n, ops)



if len(sys.argv) > 1: 
    inp = open(sys.argv[1]) 
else: 
    inp = sys.stdin

ncases = int(inp.readline())
for n in range(ncases):
    do_case(n+1)
