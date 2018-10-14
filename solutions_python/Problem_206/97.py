import sys
from collections import Counter
import itertools
import numpy as np


def get_line(format, line=None, extract_if_one=True):
    line = next(sys.stdin) if line is None else line
    types = {
        'i': int,
        'f': float,
        's': str,
    }
    line = line.strip().split(' ')
    assert len(line) == len(format)
    for i, t in enumerate(format):
        line[i] = types[t](line[i])
    return tuple(line) if len(line) > 1 or not extract_if_one else line[0]

class Problem:
    def __init__(self):
        d, n = get_line('ii')
        max_t = 0
        for i in range(n):
            k, s = get_line('ii')
            t = (d - k) / s
            max_t = max(t, max_t)
        self.ans = d / max_t

    def solve(self):
        print('%.8f' % self.ans)


def main():

    sys.stdin = open('A-large.in', 'r')
    sys.stdout = open('a.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
