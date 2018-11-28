
import collections
import itertools
import math
import networkx as nx
import numpy as np

if __name__ != '__main__':
    import devtools

################################################################################

def read_case(r):
    S, K = r.read_strs()
    return [x == '+' for x in S], int(K)

def solve_small(case):
    S, K = case
    res = 0
    for i in range(len(S) - K + 1):
        if not S[i]:
            for j in range(1, K):
                S[i+j] = not S[i+j]
            res += 1
    if all(S[-(K-1):]):
        return res
    return 'IMPOSSIBLE'

def solve_large(case):
    return solve_small(case)

def write_case(w, res):
    w.write_str(res)

################################################################################

class CaseReader(object):
    def __init__(self, f):
        self.f = f

    def __iter__(self):
        def iter():
            T = self.read_int()
            for i in range(1, T+1):
                yield i, read_case(self)
        return iter()

    def read_str(self):
        return next(self.f).strip()

    def read_int(self, b=10):
        return int(self.read_str(), b)

    def read_chrs(self):
        return list(self.read_str())

    def read_digits(self, b=10):
        return [int(x, b) for x in self.read_chrs()]

    def read_strs(self, d=' '):
        return self.read_str().split(d)

    def read_ints(self, b=10, d=' '):
        return [int(x, b) for x in self.read_strs(d)]

    def read_floats(self, d=' '):
        return [float(x) for x in self.read_strs(d)]

    def read_arr(self, rows, read_kind=read_ints, *args, **kwargs):
        return [read_kind(self, *args, **kwargs) for _ in range(rows)]

class ResWriter(object):
    def __init__(self, f, case_reader, solver=solve_small):
        self.f = f
        self.case_reader = case_reader
        self.solver = solver

    def __iter__(self):
        def iter():
            for i, case in self.case_reader:
                res = self.solver(case)
                self.f.write("Case #%d: "%i)
                write_case(self, res)
                self.f.write('\n')
                yield i, case, res
        return iter()

    @staticmethod
    def _strb(i, b):
        if i == 0:
            return 0
        s = []
        while i > 0:
            s.append(str(i%b))
            i = i//b
        return ''.join(s)

    def write_str(self, res):
        self.f.write(str(res))

    def write_int(self, res, b=10):
        self.f.write(self._strb(res, b))

    def write_strs(self, res, d=' '):
        self.f.write(d.join(str(r) for r in res))

    def write_chars(self, res, d=''):
        self.write_strs(res, d)

    def write_ints(self, res, b=10, d=' '):
        self.f.write(d.join(self._strb(r, b) for r in res))

    def write_arr(self, arr, write_kind, *args, **kwargs):
        first = True
        for row in arr:
            if first:
                first = False
            else:
                self.f.write('\n')
            write_kind(self, row, *args, **kwargs)

if __name__ == '__main__':
    in_fn = 'test-small-attempt0.in'
    out_fn = 'test-small-attempt0.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            collections.deque(ResWriter(fo, CaseReader(fi)), 0)
else:
    from run import *
