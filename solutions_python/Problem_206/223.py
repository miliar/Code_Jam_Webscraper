#!/usr/bin/python

def solve(case_no):
    d, n = map(int, raw_input().split())
    horses = [tuple(map(int, raw_input().split())) for _ in xrange(n)]
    max_time = max(map(lambda (k, s): 1.0 * (d - k) / s, horses))
    ans = d / max_time
    print 'Case #%d: %.6f' % (case_no, ans)

t = int(raw_input())
for case_no in xrange(1, t+1):
    solve(case_no)
