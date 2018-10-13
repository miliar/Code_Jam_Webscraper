#!/usr/bin/python

from operator import mul

def solve(case_no):
    n, k = map(int, raw_input().split())
    u = float(raw_input())
    p = map(float, raw_input().split())
    for _ in xrange(1000):
        current_min = min(p)
        ex_min = filter(lambda x: x > current_min, p)
        if len(ex_min) > 0:
            next_min = min(ex_min)
            count_min = len(filter(lambda x: x == current_min, p))
            addition = min(next_min - current_min, u / count_min)
            u -= addition * count_min
            p = map(lambda x: x + addition if x == current_min else x, p)
        else:
            addition = u / n;
            p = map(lambda x: x + addition, p)
            u = 0
            break
    ans = reduce(mul, p, 1.0)
    print 'Case #%d: %.6f' % (case_no, ans)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
