#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
""" 

"""
import logging

log = logging.getLogger(__name__)

class RecycledNumbers(object):

    LIMIT = 2000000

    def __init__(self):
        self.generated = {}
        self.pregen()

    def pregen(self):
        for i in xrange(1, self.LIMIT):
            self.generated[i] = []
            for N, M in self.indv(i):
                self.generated[i].append(M)

    def sol(self, A, B):
        count = 0
        for N in xrange(A, B):
            for M in self.generated[N]:
                if M <= B:
                    count += 1
        return count

    def indv(self, N):
        s = str(N)
        K = len(s)
        count = 0
        added = set()
        for i in xrange(0, K - 1):
            if s[i + 1] != "0":
                s_ = s[i+1:] + s[:i + 1]
                M = int(s_)
                if N < M and M <= self.LIMIT and not M in added:
                    added.add(M)
                    yield (N, M)

def test_cases(input):
    fi = open(input, "r")
    T = int(fi.next())
    for i in xrange(1, T+1):
        A, B = fi.next().split()
        yield i, int(A), int(B)
    fi.close()

def main(input, output):
    fo = open(output, "w")
    recycled = RecycledNumbers()
    for i, A, B in test_cases(input):
        result = recycled.sol(A, B)
        fo.write("Case #{0}: {1}\n".format(i, result)) 
    fo.close()
        
if __name__ == "__main__":
    # Parse command options
    from optparse import OptionParser
    parser = OptionParser(usage="Usage: %prog [options] param1 param2")    
    parser.add_option("-i", "--input", dest="input", help="Input file")
    parser.add_option("-o", "--output", dest="output", help="Output file")
    options, args = parser.parse_args()
    main(options.input, options.output)
