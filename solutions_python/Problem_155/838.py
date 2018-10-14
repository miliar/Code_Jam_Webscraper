import sys
rl = lambda: sys.stdin.readline().strip()

T = int(rl())

for tcase in range(1, T + 1):
    smax, ss = rl().split()
    ss = [int(s) for s in ss]
    smax = int(smax)
    accum = 0
    ans = 0
    for need, s in enumerate(ss):
        if accum < need:
            ans += (need - accum)
            accum += (need - accum)
        accum += s
    print 'Case #%d: %d' % (tcase, ans)
