import sys
from collections import Counter
import itertools
import numpy as np


def get_line(format, line=None):
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
    return tuple(line) if len(line) > 1 else line[0]


class Problem:
    def print_map(self, m):
        model_code_rev = {0: '.', 1: 'x', 2: '+', 3: 'o'}
        for l in m:
            print(''.join(list(map(lambda x: model_code_rev[x], l))))
        print()

    def cross_path(self, k):
        for j in self.edge_list[k]:
            if self.used[j] == 0:
                self.used[j] = 1
                if self.match[j] < 0 or self.cross_path(self.match[j]):
                    self.match[j] = k
                    return True
        return False

    def hungary(self):
        self.match_cnt = 0
        self.used = np.zeros(2*self.n-1, dtype=np.int)
        for i in range(2*self.n-1):
            if self.cross_path(i):
                self.match_cnt += 1
            self.used = self.used * 0

    def __init__(self):
        n, m = get_line('ii')
        self.n = n
        self.m = m
        self.diag_cnt = n * 2 - 1
        self.map = np.zeros((n, n), dtype=np.int)
        self.valid_row = list(range(n))
        self.valid_col = list(range(n))
        self.valid_diaga = list(range(2*n-1))
        self.valid_diagb = list(range(-n+1, n))
        model_code = {'.': 0, 'x': 1, '+': 2, 'o': 3}
        model_code_rev = {0: '.', 1: 'x', 2: '+', 3: 'o'}
        for i in range(m):
            ch, x, y = get_line('sii')
            x, y = x-1, y-1
            ch = model_code[ch]
            if ch & 1 > 0:
                self.map[x][y] |= 1
                self.valid_row.remove(x)
                self.valid_col.remove(y)
            if ch & 2 > 0:
                self.map[x][y] |= 2
                self.valid_diaga.remove(x+y)
                self.valid_diagb.remove(x-y)
        self.new_map = np.copy(self.map)

        # build graph
        self.match = np.ones(self.diag_cnt, dtype=np.int) * -1
        self.edge_list = [[] for i in range(self.diag_cnt)]
        for a, b in itertools.product(self.valid_diaga, self.valid_diagb):
            x, y = (a + b) / 2, (a - b) / 2
            if (a+b) % 2 == 1 or x < 0 or y < 0 or x >= n or y >= n:
                continue
            b -= (-n+1)
            self.edge_list[a].append(b)
        self.hungary()

        for i in range(self.diag_cnt):
            if self.match[i] >= 0:
                a, b = self.match[i], i + (-n+1)
                x, y = int((a + b) / 2), int((a - b) / 2)
                self.new_map[x][y] |= 2

        while len(self.valid_row) > 0 and len(self.valid_col) > 0:
            x = self.valid_row[0]
            y = self.valid_col[0]
            self.new_map[x][y] |= 1
            self.valid_row.remove(x)
            self.valid_col.remove(y)

        self.ans1 = 0
        self.ans2 = 0
        self.ans_list = []
        for i in range(n):
            for j in range(n):
                if 1 & self.new_map[i][j]:
                    self.ans1 += 1
                if 2 & self.new_map[i][j]:
                    self.ans1 += 1
                if self.map[i][j] != self.new_map[i][j]:
                    self.ans2 += 1
                    md = model_code_rev[self.new_map[i][j]]
                    self.ans_list.append((md, i+1, j+1))

    def solve(self):
        # print()
        # self.print_map(self.map)
        # self.print_map(self.new_map)
        print(self.ans1, self.ans2)
        for l in self.ans_list:
            print(' '.join(list(map(str, l))))


def main():
    sys.stdin = open('D-large.in', 'r')
    sys.stdout = open('dlarge.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
