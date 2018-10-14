#!/usr/bin/env python

from __future__ import absolute_import
import sys
import unittest
from StringIO import StringIO
import numpy as np

sample_in = \
"""
4
++-- 3
---+-++- 3
+++++ 4
-+-+- 4
"""[1:]

sample_out = \
"""
Case #1: IMPOSSIBLE
Case #2: 3
Case #3: 0
Case #4: IMPOSSIBLE
"""[1:]


def run(in_buf=sys.stdin, out_buf=sys.stdout):

    cases = int(in_buf.readline())

    for c in xrange(1, cases+1):

        out_buf.write("Case #%s: " % c)

        stack,k = [s for s in in_buf.readline().split(" ")]
        stack = [s for s in stack]
        k = int(k)
        slen = len(stack)

        count = 0

        while '-' in stack:
            i = stack.index('-')

            if i < slen-k:
                for j in xrange(k):
                    stack[i+j] = ('-' if stack[i+j] is '+' else '+')
                count += 1
            elif i == slen - k:
                # check impossible
                pop = stack[i:]
                if '+' in pop:
                    #impossible
                    count = -1
                else:
                    #possible, dont need to actually flip
                    count += 1

                break

            else:
                # impossible
                count = -1
                break

        if count >= 0:
            out_buf.write("{}\n".format(count))
        else:
            out_buf.write("IMPOSSIBLE\n")

class Case2017QA(unittest.TestCase):

    def test_run(self):
        for i in xrange(1000):
            sample_in_buf = StringIO(sample_in)
            output = StringIO()
            run(sample_in_buf, output)
            self.assertSequenceEqual(sample_out.splitlines(), output.getvalue().splitlines())


if __name__ == '__main__':
    run()

