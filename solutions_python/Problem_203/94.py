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
    n, m = next_int()
    cake = []
    for i in range(n):
        cake.append(next_line())
    return n, m, cake

def solve(inp):
    n, m, cake = inp
    newcake = []
    res = ""
    for row in cake:
        newrow = ""
        for i in range(len(row)):
            if row[i] == '?':
                newrow += helper(row, i)
            else:
                newrow += row[i]
        newcake.append(newrow)
    newcake2 = []
    for i in range(len(newcake)):
        newcake2.append(helper2(newcake, i))
    for r in newcake2:
        res += "\n" + r
    return res



def helper(row: str, i):
    c = i
    while c< len(row) and row[c] == '?':
        c+=1
    if c == len(row):
        c-=1
        while c>=0 and row[c] == '?':
            c-=1
    if c==-1:
        return '?'
    return row[c]

def helper2(cake, i):
    c = i
    while c< len(cake) and cake[c][0] == '?':
        c+=1
    if c == len(cake):
        c-=1
        while c>=0 and cake[c][0] == '?':
            c-=1
    return cake[c]


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
