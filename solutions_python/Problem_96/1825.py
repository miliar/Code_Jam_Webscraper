from __future__ import division
import itertools as it
from sys import stdin

def solve(N, S, p, ts):
    res = 0
    for t in ts:
        a = p
        b = (t-a) // 2
        c = t - a - b
        if b < 0 or c < 0: continue
        if b >= p-1 and c >= p-1:
            res += 1
        elif b >= p-2 and c >= p-2 and S > 0:
            res += 1
            S -= 1
    return res
    
def main():
    T = int(next(stdin))
    res = 1
    for i, line in enumerate(stdin):
        xs = map(int, line.split())
        N, S, p = xs[:3]; ts = xs[3:]
        print 'Case #%d: %s' % (i+1, solve(N, S, p, ts))
    
if __name__ == '__main__':
    main()
