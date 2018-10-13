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
        n, p = get_line('ii')
        g = get_line('i'*n)
        try:
            g = list(map(lambda x: x % p, g))
        except:
            g = [g]
            g = list(map(lambda x: x % p, g))
        d = {}
        for i in range(p):
            d[i] = 0
        for x in g:
            d[x] += 1

        ans = d[0]
        d[0] = 0

        if p == 2:
            ans += (d[1] + 1) // 2
            self.ans = ans
            return
        elif p == 3:
            x = min(d[1], d[2])
            ans += x
            d[1] -= x
            d[2] -= x
            ans += (d[1] + d[2] + 2) // 3
            self.ans = ans
            return
        elif p == 4:
            x = min(d[1], d[3])
            ans += x
            d[1] -= x
            d[3] -= x

            x = min(d[1]//2, d[2])
            ans += x
            d[1] -= 2*x
            d[2] -= x

            x = min(d[3]//2, d[2])
            ans += x
            d[3] -= 2*x
            d[2] -= x

            x = d[2] // 2
            ans += x
            d[2] -= 2*x

            x = d[1] // 4
            ans += x
            d[1] -= 4*x

            x = d[3] // 4
            ans += x
            d[3] -= 4*x

            x = d[1] + d[2] + d[3]
            if x > 0:
                ans += 1
            self.ans = ans
        return


    def solve(self):
        print(self.ans)


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
