#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

MAX=10
dp = {}
dps = {}
for p1 in xrange(MAX+1):
    for p2 in xrange(p1, p1+3):
        if p2 > MAX: break
        for p3 in xrange(p1, p1+3):
            if p3 > MAX: break
            summ = p1 + p2 + p3
            maxx = max(p1, p2, p3)
            minn = min(p1, p2, p3)
            if maxx - minn > 1:
                #surprising
                dps[summ] = dps.get(summ, maxx)
            else:
                #regular score
                dp[summ] = dp.get(summ, maxx)


def doit(N, S, p, points):
    points = sorted(points)
    ans = 0
    for point in points:
        #try regular score
        max_score = dp[point]
        if max_score >= p:
            ans += 1
        elif S > 0 and 2 <= point <= 28:
            #try surprising score
            max_score = dps[point]
            if max_score >= p:
                S -= 1
                ans += 1
                
    return ans

if __name__ == '__main__':
    C = readint()
    for c in xrange(1, C+1):
        params = readlinearray(int)
        N, S, p, points = params[0], params[1], params[2], params[3:]
        ans = doit(N, S, p, points)
        print 'Case #%d: %s' % (c, ans)
