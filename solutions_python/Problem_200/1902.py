#!/usr/bin/env python

from __future__ import absolute_import
import sys
import unittest
from StringIO import StringIO
import numpy as np

sample_in = \
"""
4
132
1000
7
111111111111111110
"""[1:]

sample_out = \
"""
Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999
"""[1:]


def run(in_buf=sys.stdin, out_buf=sys.stdout):

    cases = int(in_buf.readline())

    for c in xrange(1, cases+1):
        out_buf.write("Case #%s: " % c)
        n = list(in_buf.readline().strip())
        n = [int(i) for i in n]

        solved = 0

        while not solved:

            solved = 1

            # strip zeros
            while not n[0]:
                n = n[1:]

            # if all same digit, is tidy
            if len(set(n)) == 1:
                break

            for i in xrange(len(n) - 1):

                if n[i] > n[i+1]:
                    n[i] -= 1

                    # 10 -> 9 semantics
                    n[i+1:] = [9] * ((len(n) - 1) - i)

                    solved = 0
                    break

        n = [str(i) for i in n]
        n = ''.join(n)
        out_buf.write("{}\n".format(n))


class Case2017QB(unittest.TestCase):

    def test_run(self):
        for i in xrange(10000):
            sample_in_buf = StringIO(sample_in)
            output = StringIO()
            run(sample_in_buf, output)
            self.assertSequenceEqual(sample_out.splitlines(), output.getvalue().splitlines())


if __name__ == '__main__':
    run()

