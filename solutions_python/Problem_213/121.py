import sys

from collections import defaultdict

class Solution(object):
    def __init__(self, n, c, m, ns):
        self.n = n
        self.m = m
        self.c = c
        assert c == 2
        self.ns = ns

    def solve(self):
        d = [ defaultdict(int), defaultdict(int), defaultdict(int) ]
        for (p, b) in self.ns:
            p = min(3, p)
            d[p - 1][b] += 1

        ans = 0
        prom = 0

        for (k0, v0) in d[0].items():
            while d[0][k0]:
                for (k1, v1) in d[1].items():
                    if k0 == k1:
                        continue
                    v = min(v0, v1)
                    ans += v
                    d[1][k1] -= v
                    d[0][k0] -= v
                else:
                    break
                    
        for (k0, v0) in d[0].items():
            while d[0][k0]:
                for (k2, v2) in d[2].items():
                    if k0 == k2:
                        continue
                    v = min(v0, v2)
                    ans += v
                    prom += v
                    d[2][k2] -= v
                    d[0][k0] -= v
                else:
                    break

        d0 = dict(filter(lambda (k, v): v != 0, d[0].items()))
        d1 = dict(filter(lambda (k, v): v != 0, d[1].items()))
        d2 = dict(filter(lambda (k, v): v != 0, d[2].items()))
        
        #print d0, d1, d2

        if d0:
            ans += sum(map(lambda (k, v): v, d0.items()))

        for (k1, v1) in d1.items():
            while d1[k1]:
                for (k2, v2) in d2.items():
                    if k1 == k2:
                        continue
                    v = min(v1, v2)
                    ans += v
                    prom += v
                    d2[k2] -= v
                    d1[k1] -= v
                else:
                    break

        if d1:
            t = map(lambda (k, v): v, d1.items())
            while t:
                if len(t) == 1:
                    ans += t[0]
                    break
                a, b = t[0], t[1]
                ans += min(a, b)
                prom += min(a, b)
                t = t[2:] + [abs(a - b)]
                
        if d2:
            t = map(lambda (k, v): v, d2.items())
            while t:
                if len(t) == 1:
                    ans += t[0]
                    break
                a, b = t[0], t[1]
                ans += min(a, b)
                prom += min(a, b) * 2
                t = t[2:] + [abs(a - b)]
        return ans, prom

def test():
    
    n, c, m = 2, 2, 2
    ns = [
        [2, 1],
        [2, 2]
    ]
    assert Solution(n, c, m, ns).solve() == (1, 1)
    
    
    n, c, m = 2, 2, 2
    ns = [
        [1, 1],
        [2, 1]
    ]
    assert Solution(n, c, m, ns).solve() == (2, 0)
    
    n, c, m = 2, 2, 2
    ns = [
        [1, 1],
        [1, 2]
    ]
    assert Solution(n, c, m, ns).solve() == (2, 0)
    

    

if __name__ == '__main__':
    test()
    
    T = int(raw_input())
    for case_ in xrange(T):
        print 'Case #%d:' % (case_ + 1),
        n, c, m = map(int, raw_input().split())
        ns = [ map(int, raw_input().split()) for i in xrange(m) ]
        print '%d %d' % Solution(n, c, m, ns).solve()

