import os
import sys
import re


class dt:
    def __init__(self, prob, name=''):
        self.prob = prob
        self.name = name
        self.left = None
        self.right = None

    def add_left(self, left):
        self.left = left

    def add_right(self, right):
        self.right = right


def read_strs():
    return f.readline().strip().split()


def read_ints():
    return list(map(int, read_strs()))


def gen_dt(lines):
    if not lines:
        return None
    line = lines[0].strip(' ()\n')
    del lines[0]
    elems = line.split()
    if len(elems) == 1:
        return dt(float(elems[0]))
    else:
        s1, s2 = elems
        tt = dt(float(s1), s2)
        tt.add_left(gen_dt(lines))
        tt.add_right(gen_dt(lines))
        while lines and lines[0].strip() == ')':
            del lines[0]
        return tt


def solve(s, t):
    p = s.split()[2:]
    tt = t
    res = 1.0
    while True:
        res *= tt.prob
        if not tt.name:
            break
        elif tt.name in p:
            tt = tt.left
        else:
            tt = tt.right
    return res


# main
with open(sys.argv[1]) as f:
    n = int(f.readline().strip())
    for i in range(1, n + 1):
        print('Case #{}:'.format(i))
        n1 = int(f.readline().strip())
        dt_str = []
        for j in range(n1):
            dt_str.append(f.readline().strip())
        t = gen_dt(dt_str)
        n2 = int(f.readline().strip())
        for j in range(n2):
            res = solve(f.readline().strip(), t)
            print(res)