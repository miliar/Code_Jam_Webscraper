"""Usage:
    pypy3 -u X.py < X-test.in > X-test.out
or sometimes:
    python3 -u X.py < X-test.in > X-test.out
"""
from __future__ import print_function

import sys


def common_setup():
    pass

import heapq as hq
class priorityDictionary(dict):
    def __init__(self):
        self.__heap = []
        dict.__init__(self)
    def smallest(self):
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            hq.heappop(heap)
        return heap[0][1]
    def __iter__(self):
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
    def __setitem__(self,key,val):
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            hq.heapify(self.__heap)
        else:
            hq.heappush(heap, (val,key))



def case_reader(tc, infile):
    P = list(map(int, next(infile).split()))
    I = [list(map(int, next(infile).split())) for _ in range(P[0])]
    T = [list(map(int, next(infile).split())) for _ in range(P[0])]
    S = [list(map(int, next(infile).split())) for _ in range(P[1])]
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):

    N, Q = P
    G = {}
    for u, i in enumerate(T):
        G[u + 1] = {}
        for v, d in enumerate(i):
            if d >= 0:
                G[u + 1][v + 1] = d
    res = []
    for start, end in S:
        D = {}  # dictionary of final distances
        Q = priorityDictionary()   # est.dist. of non-final vert.
        Q[(start, I[start - 1][0], I[start - 1][1])] = 0

        for state in Q:
            D[state] = Q[state]
            v, e, s = state
            if v == end:
                res.append(D[state])
                break

            for w in G[v]:
                ee = e - G[v][w]
                if ee >= 0:
                    wLength = D[state] + G[v][w] / s
                    if (w, ee, s) not in Q or wLength < Q[(w, ee, s)]:
                        Q[w, ee, s] = wLength
                el, sl = I[v - 1]
                ee = el - G[v][w]
                if ee >= 0:
                    wLength = D[state] + G[v][w] / sl
                    if (w, ee, sl) not in Q or wLength < Q[(w, ee, sl)]:
                        Q[w, ee, sl] = wLength
    return 'Case #{:d}: {}'.format(tc, ' '.join(f'{d}' for d in res))


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
