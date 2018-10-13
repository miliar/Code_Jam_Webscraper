#!/usr/bin/env python2
import itertools
def solve(n, p, r, q):
    for qi in q:
        qi.sort()
        qi.reverse()
    pkgs = 0
    for size in itertools.count(1):
        while True:
            for qi, ri in zip(q, r):
                g_100 = size * ri
                g_90 = g_100 * 90
                g_110 = g_100 * 110
                while qi and qi[-1] * 100 < g_90:
                    qi.pop()
                if not qi:
                    return pkgs
                if qi[-1] * 100 > g_110:
                    break
            else:
                for qi in q:
                    qi.pop()
                pkgs += 1
                continue
            break
def main():
    for t in xrange(1, 1 + int(raw_input())):
        print 'Case #%d:' % t,
        n, p = map(int, raw_input().split())
        r = map(int, raw_input().split())
        q = [map(int, raw_input().split()) for _ in xrange(n)]
        assert len(r) == n
        assert len(q) == n
        assert all(len(qi) == p for qi in q)
        print solve(n, p, r, q)
if __name__ == '__main__':
    main()
