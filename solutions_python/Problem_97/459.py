#!/usr/bin/python
import sys

maxb = 2000000

count = [0 for dummy in range(maxb + 1)]
csum = [0 for dummy in range(maxb + 1)]

def precalc():
    for n in xrange(1, maxb + 1):
        s = str(n)
        l = len(s)
        seen = set()
        for j in range(l):
            ss = s[j:] + s[:j]
            if ss[0] == '0':    continue
            m = int(ss)
            if m > n and m not in seen:
                seen.add(m)
                count[n] = count[n] + 1
        csum[n] = csum[n - 1] + count[n]

def solve(a, b):
    if a >= b:  return 0
    ans = 0
    for n in xrange(a, b + 1):
        s = str(n)
        l = len(s)
        seen = set()
        for j in range(l):
            ss = s[j:] + s[:j]
            if ss[0] == '0':    continue
            m = int(ss)
            if m > n and m <= b and m not in seen:
                seen.add(m)
                ans = ans + 1
    return ans

precalc()
T = int(sys.stdin.readline())
for i in range(T):
    s = sys.stdin.readline().split(' ')
    a, b = int(s[0]), int(s[1])
    cs = '1'
    for j in range(1, len(str(b))):
        cs = cs + '0'
    c = int(cs)
    if c <= a:
        ans = solve(a, b)
    else:
        ans = csum[c] - csum[a - 1] + solve(c, b)
    print 'Case #%d: %d' % (i + 1, ans)

