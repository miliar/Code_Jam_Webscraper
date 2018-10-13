#! /usr/bin/env python
import heapq
from numpy import * # http://www.scipy.org/
import psyco # http://psyco.sourceforge.net/
psyco.full()

class Case(object):
    def __init__(self, *a):
        self.a = a

    @classmethod
    def read(self, read):
        n = int(read())
        return self(tuple(int(x) for x in read().split()),
                    tuple(int(x) for x in read().split()))

    def solve(self):
        v1, v2 = map(sorted, self.a)
        n = len(v1)
        a = array([v1] * n, dtype=int64)
        b = array([v2] * n, dtype=int64).transpose()
        mat = a * b
        del a, b

        hpush = heapq.heappush
        hpop = heapq.heappop
        pq = []
        hpush(pq, (0, 0, ()))
        best = None
        while pq:
            idx, s, used = hpop(pq)
            bestest = s + sum(min(row) for row in mat[-idx:])
            if best is None or bestest < best:
                if idx == -n:
                    best = s
                else:
                    for j in xrange(n):
                        if j in used:
                            continue
                        hpush(pq, (idx - 1, s + mat[-idx][j], used + (j,)))
        return best

if __name__ == '__main__':
    read = raw_input
    for i in xrange(int(read())):
        print 'Case #%d:' % (i + 1), Case.read(read).solve()
