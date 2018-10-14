from collections import defaultdict

def solve(N, K):
    d = defaultdict(int)
    d[N] = 1
    while len(d) > 0:
        space = max(d.keys())
        c = d[space]
        del d[space]
        l = (space - 1) / 2
        r = space / 2
        if l > 0: d[l] += c
        if r > 0: d[r] += c
        K -= c
        if K <= 0:
            return '%d %d' % (r, l)

    return 'ERROR'

import sys
sys.stdin = open('C-large.in', 'rt')
sys.stdout = open('C-large.out', 'wt')

T = int(raw_input().strip())
for t in xrange(1, T+1):
    N, K = map(int, raw_input().strip().split(' '))
    print "Case #%d: %s" % (t, solve(N, K))
