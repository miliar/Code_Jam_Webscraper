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
        n, q = get_line('ii')
        self.n = n
        self.q = q
        e = np.zeros(n, dtype=np.int64)
        self.e = e
        self.s = s
        s = np.zeros(n, dtype=np.int64)
        self.s = s
        adj = np.zeros((n, n), dtype=np.int64)
        self.adj = adj
        for i in range(n):
            e[i], s[i] = get_line('ii')
        for i in range(n):
            adj[i, :] = np.array(get_line('i'*n), dtype=np.int64)
        # print(adj)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adj[i, k] > -1 and adj[k, j] > -1:
                        if adj[i, j] == -1 or adj[i, j] > adj[i, k] + adj[k, j]:
                             adj[i, j] = adj[i, k] + adj[k, j]

    def solve(self):
        print()
        pass
        # print(self.ans)
def main():

    sys.stdin = open('C-small-attempt1.in', 'r')
    sys.stdout = open('c.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
