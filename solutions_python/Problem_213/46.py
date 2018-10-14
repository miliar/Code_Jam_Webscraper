import sys
from collections import Counter
import itertools
import numpy as np
from collections import defaultdict


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
        n, c, m = get_line('iii')
        self.n = n
        self.c = c
        self.m = m
        d = defaultdict(list)
        ride = 0
        pos_cnt = np.zeros((n+1,), dtype=np.int32)
        for i in range(m):
            pi, bi = get_line('ii')
            d[bi].append(pi)
            ride = max(ride, len(d[bi]))
            pos_cnt[pi] += 1

        pos_cnt_sum = np.zeros((n+1,), dtype=np.int32)
        for i in range(1, n+1):
            pos_cnt_sum[i] = pos_cnt_sum[i-1] + pos_cnt[i]
            if i * ride < pos_cnt_sum[i]:
                ride = pos_cnt_sum[i] // i
                if pos_cnt_sum[i] % i != 0:
                    ride += 1
        prom = 0
        for i in range(1, n+1):
            if pos_cnt[i] > ride:
                prom += pos_cnt[i] - ride
        self.prom = prom
        self.ride = ride


    def try_arrange(self, pos, run, cospos):
        if self.arr[pos][run] == 0:
            self.arr[pos][run] = 1
            cospos.remove(pos)
            return run, 0

        for i in range(run, self.m+2):
            for j in range(pos, 0, -1):
                if self.arr[j][i] == 0:
                    self.arr[j][i] = 1
                    if j in cospos:
                        cospos.remove(j)
                        return i, 0
                    else:
                        cospos.remove(cospos[0])
                        return i, 1
        assert False
        return None

    def solve(self):
        print(self.ride, self.prom)


def main():

    sys.stdin = open('B-large.in', 'r')
    sys.stdout = open('b.out', 'w')
    T = get_line('i')
    for i in range(T):
        print('Case #%d: ' % (i+1, ), end='')
        p = Problem()
        p.solve()


if __name__ == '__main__':
    main()
