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

    def __init__(self):
        n, m = get_line('ii')
        self.n = n
        self.m = m
        self.map = []
        for i in range(n):
            self.map.append(list(get_line('s')))
        fl = None
        for line in self.map:
            charset = set(line)
            if '?' in charset:
                charset.remove('?')
            exist_char = (len(charset) > 0)
            if not exist_char:
                continue
            else:
                for x in line:
                    if x != '?':
                        fc = x
                        break
                for i in range(len(line)):
                    if line[i] == '?':
                        line[i] = fc
                    else:
                        fc = line[i]
                if fl is None:
                    fl = list(line)
        for i, line in enumerate(self.map):
            if line[0] == '?':
                self.map[i] = list(fl)
            else:
                fl = list(line)



    def solve(self):
        print()
        for l in self.map:
            print(''.join(l))


def main():

    sys.stdin = open('A-large.in', 'r')
    sys.stdout = open('A-large.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
