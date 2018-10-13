#!/usr/bin/env python2

from multiprocessing import Pool, cpu_count
from functools import partial
import operator
import pudb

pool = Pool(processes = cpu_count())

def powerset(seq):
    """
    Generate the powerset from a sequence.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

nc = int(raw_input())
for c in xrange(nc):
    s = map(int,raw_input().split())
    n = s.pop(0)

    ans = []
    sums = {}
    for i in powerset(s):
        sum_i = sum(i)
        if sum_i in sums:
            ans.append(sums[sum_i])
            ans.append(i)
            break
        sums[sum_i] = i

    if len(ans) > 0:
        print "Case #%d:" % (c+1)
        for a in ans:
            for i in a:
                print i,
            print
    else:
        print "Case #%d:" % (c+1)
        print "Impossible"
