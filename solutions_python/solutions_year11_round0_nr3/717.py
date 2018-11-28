#!/usr/bin/env python

import sys
import select
import operator


def make_case(n, line):
    # The first line of the input gives the number of test cases, T. T
    # test cases follow. Each test case is described in two lines. The
    # first line contains a single integer N, denoting the number of
    # candies in the bag. The next line contains the N integers Ci
    # separated by single spaces, which denote the value of each piece
    # of candy in the bag.

    return map(long, line.split()[:n])


def test_result(case):

    result = map(lambda (s1, s2): max(sum(s1), sum(s2)),
                 filter(lambda (s1, s2): (reduce(operator.xor, s1) == reduce(operator.xor, s2)),
                        map(lambda s: ([case[c] for c in xrange(len(case)) if c in s],
                                       [case[c] for c in xrange(len(case)) if c not in s]),
                            filter(lambda s: len(s) > 0 and len(s) < len(case),
                                   map(set, reduce(lambda result, x: result + [subset + [x] for subset in result], xrange(len(case)), [[]]))))))

    return max(result) if result else 'NO'


if __name__ == "__main__":
    
    try:
        try:
            data = open(sys.argv[1])
        except:
            data = sys.stdin
        if select.select([data,],[],[],0.0)[0]:
            lines = data.readlines()
        T = int(lines[0])
    except:
        sys.exit('Usage: %(file)s input-filename' % dict(file=__file__))

    for t in xrange(1, T+1):
        n = int(lines[2*t-1])
        line = lines[2*t]
        print 'Case #%d: %s' % (t, test_result(make_case(n, line)))
