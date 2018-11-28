#!/usr/bin/env python

import math
import multiprocessing
import itertools
import sys

#from ipdb import launch_ipdb_on_exception


def ints():
    return [int(x) for x in raw_input().strip().split()]


class TestCase(object):
    """
    Template for solving test cases
    """
    def __init__(self, idx):
        self.idx = idx
        self.parse()

    def parse(self):
        """
        Called synchronously in order to parse data from stdin
        """
        self.r, self.t = ints()

    def volume(self, nth):
        return 4*nth + 2*self.r + 1

    def totvol(self, n):
        #return (n+1) * (4*n + 4*self.r + 2)/2
        return ((2*n)*n + (2*self.r + 3)*n + 2*self.r + 1)

    def _nrings(self):
        a = 2.
        b = 2.*self.r + 3
        c = 2.*self.r + 1 - self.t
        det = math.sqrt(b**2 - 4*a*c)
        return int((max(((-b + m*det)/(2*a)) for m in [-1, 1]))+1)

    def nrings(self):
        n = self._nrings()
        if self.totvol(n-1) > self.t:
            #print self.totvol(n), ">", self.t
            return n - 1
        return n

    @property
    def result(self):
        """
        IMPLEMENT ME
        """
        return str(self.nrings())

    def __str__(self):
        return 'Case #{self.idx}: {self.result}'.format(self=self)


if __name__ == '__main__':
    solvers = []
    ncases = input()
    for i in xrange(ncases):
        solvers.append(TestCase(i+1))

    if 'debug' in sys.argv:
        pool = itertools
    else:
        pool = multiprocessing.Pool(4)

    for soln in pool.imap(str, solvers):
        print soln
    if 'debug' not in sys.argv:
        pool.close()
        pool.join()
