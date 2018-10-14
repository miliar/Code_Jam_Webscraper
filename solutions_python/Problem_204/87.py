# python 3.6
import numpy as np
import math
import networkx as nx
import fractions
from functools import reduce
import time
import fileinput
import multiprocessing


def read():
    n, p = next_int()
    r = [int(s) for s in next_line().split()]
    q = []
    for i in range(n):
        q.append([int(s) for s in next_line().split()])
    return n, p, r, q

def solve(inp):
    n, p, r, q = inp
    for row in q:
        row.sort()
    q1 = []
    for i, row in enumerate(q):
        q1.append([])
        for x in row:
            y = (math.ceil(x/r[i]/1.1), math.floor(x/r[i]/0.9))
            if y[0]<=y[1]:
                q1[len(q1)-1].append(y)
    if len(q1) == 1:
        return len(q1[0])
    res = 0
    for x in q1[0]:
        can = [True] + [False] * (n-1)
        for i,row in enumerate(q1):
            if i==0:
                continue
            for y in row:
                if is_pair(x, y):
                    can[i] = True
        if can == [True] * n:
            res += 1
            for i, row in enumerate(q1):
                if i == 0:
                    continue
                for y in row:
                    if is_pair(x, y):
                        row.remove(y)
                        break


    #res = ""

    return  res

def is_pair(a,b):
    return a[0]<=b[1] and a[1]>=b[0]

def main():
    t = next_int()  # read a line with a single integer
    inputs = []
    for case_number in range(1, t + 1):
        inputs.append(read())
    k = multiprocessing.cpu_count()
    p = multiprocessing.Pool(k)
    outputs = list(map(solve, inputs))
    for case_number, res in enumerate(outputs):
        print("Case #{}: {}".format(case_number + 1, res))


def is_in_map(i, j, m, n):
    return 0 <= i < m and 0 <= j < n


def create_file_line_iterator():
    for line in fileinput.input():
        yield line


def next_line():
    return next(fileLineIterator).strip()


def next_int():
    next_ints_line = next_line().split()
    return [int(s) for s in next_ints_line] if len(next_ints_line) > 1 else int(next_ints_line[0])


class MyFraction(object):
    def __init__(self, n, d):
        if d == 0:
            self.npa = np.nan
        else:
            gcd = math.gcd(n, d)
            gcd *= 1 if d > 0 else -1
            n1, d1 = n // gcd, d // gcd
            self.npa = np.array([n1, d1], dtype=np.int64)

    def __eq__(self, other):
        return self.npa[0] == other.npa[0] and self.npa[1] == other.npa[1]

    def __cmp__(self, other):
        r = self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0]
        if r < 0:
            return -1
        if r > 0:
            return 1
        return 0

    def __lt__(self, other):
        return self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0] < 0

    def __le__(self, other):
        return self.npa[0] * other.npa[1] - self.npa[1] * other.npa[0] <= 0


fileLineIterator = create_file_line_iterator()
if __name__ == '__main__':
    main()
