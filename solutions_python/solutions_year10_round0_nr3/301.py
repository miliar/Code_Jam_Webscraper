#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import itertools as it


def solve(r, k, groups):
    indexes = []
    passengers = []
    
    ngi = 0
    loopindex = None
    for ride in range(r):
        p, dest = calculate(ngi, k, groups)
        if ngi not in indexes:
            indexes.append(ngi)
            passengers.append(p)
            ngi = dest
        else:
            loopindex = indexes.index(ngi)
            break

    if loopindex is not None:
        prefix = passengers[:loopindex]
        midfix = passengers[loopindex:]
        suffix = passengers[loopindex:loopindex+(r-len(prefix))%len(midfix)]
        return sum(prefix) + (sum(midfix) * ((r-len(prefix)) / len(midfix))) + sum(suffix)
    else:
        return sum(passengers)


def calculate(fgi, k, groups):
    grouplen = len(groups)
    ngi = fgi
    remaining = k
    while remaining >= groups[ngi]:
        remaining -= groups[ngi]
        ngi += 1
        if ngi == grouplen:
            ngi = 0
        if ngi == fgi:
            break
    return (k-remaining, ngi)


def main(argv=sys.argv[1:]):
    fin = open(argv[0], 'r')
    fout = open(argv[1], 'w')

    test_count = int(fin.readline().strip())
    for index in range(test_count):
        r,k,n = [int(v) for v in fin.readline().strip().split()]
        groups = [int(v) for v in fin.readline().strip().split()]
        result = solve(r, k, groups)
        print 'Case #%d: %d' % (index+1, result)
        print >> fout, 'Case #%d: %d' % (index+1, result)


def profile():
    import random, timeit
    g = [random.randint(1e6,int(1e7)) for i in range(1000)]
    print 'Starting...'
    t = timeit.Timer('solve(int(1e8),int(1e9),%r)'%g, "from __main__ import solve")
    times = 10
    print t.timeit(times)/times


def profile3():
    import random
    g = [random.randint(1,int(1e7)) for i in range(1000)]
    solve(int(1e7),int(1e9), g)


def test():
    print '%d %d' % (21, solve(4, 6, [1,4,2,1]))
    print '%d %d' % (25, solve(5, 6, [1,4,2,1]))
    print '%d %d' % (0, solve(0, 0, []))
    print '%d %d' % (0, solve(1, 1, [4]))
    print '%d %d' % (100, solve(100, 10, [1]))
    print '%d %d' % (20, solve(5, 5, [2,4,2,3,4,2,1,2,1,3]))
    
if __name__ == '__main__':
    main()