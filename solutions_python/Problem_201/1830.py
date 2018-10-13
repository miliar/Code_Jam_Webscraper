#!/usr/bin/env python

from __future__ import absolute_import
import sys
import unittest
from StringIO import StringIO


sample_in = \
"""
5
4 2
5 2
6 2
1000 1000
1000 1
"""[1:]

sample_out = \
"""
Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499
"""[1:]


def run(in_buf=sys.stdin, out_buf=sys.stdout):

    cases = int(in_buf.readline())

    for c in xrange(1, cases+1):
        out_buf.write("Case #%s: " % c)
        N,K = [int(s) for s in in_buf.readline().split(" ")]

        max_min = 0
        max_max = 0

        stalls = [0]*N
        deltas = []
        for j in xrange(N):
            deltas.append([0, 0])

        for i in xrange(K):

            l = 0
            r = 0

            for j in xrange(N):

                if not stalls[j]:
                    deltas[j][0] = l
                    l += 1
                else:
                    l = 0

                if not stalls[-(j+1)]:
                    deltas[-(j+1)][1] = r
                    r += 1
                else:
                    r = 0

            dist = [[ind, min(m), max(m)] for ind, m in enumerate(deltas) if not stalls[ind]]

            max_min = max([x[1] for x in dist])

            dist = [d for d in dist if d[1] == max_min]

            if len(dist) > 1:
                max_max = max([x[2] for x in dist])
                dist = [d for d in dist if d[2] == max_max]
            elif not len(dist):
                print "FAIL"

            max_min = dist[0][1]
            max_max = dist[0][2]

            pos = dist[0][0]
            stalls[pos] = 1

        out_buf.write("{} {}\n".format(max_max, max_min))


class Case2017QC(unittest.TestCase):

    def test_run(self):
        for i in xrange(20):
            sample_in_buf = StringIO(sample_in)
            output = StringIO()
            run(sample_in_buf, output)
            self.assertSequenceEqual(sample_out.splitlines(), output.getvalue().splitlines())


if __name__ == '__main__':
    run()

