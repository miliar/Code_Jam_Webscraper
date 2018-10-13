#!/usr/bin/env python

import sys

def solve():
    numbers = [int(w) for w in sys.stdin.readline().split()[1:]]
    sums = {}
    for n in numbers:
        sums[n] = [set([n])]
    for sum in sorted(sums.keys()):
        for combination in sums[sum]:
            for sum2 in sorted(sums.keys()):
                for combination2 in sums[sum2]:
                    if not combination.intersection(combination2):
                        newvalue = combination.union(combination2)
                        if sum + sum2 in sums:
                            for test in sums[sum + sum2]:
                                if not test.intersection(newvalue):
                                    return newvalue, test
                            sums[sum + sum2].append(newvalue)
                        else:
                            sums[sum + sum2] = [newvalue]

for tc in xrange(1, int(sys.stdin.readline()) + 1):
    (s1, s2) = solve()
    print 'Case #%d:' % (tc)
    print ' '.join([str(w) for w in s1])
    print ' '.join([str(w) for w in s2])
