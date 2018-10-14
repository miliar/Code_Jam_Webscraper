import sys
rl = lambda: sys.stdin.readline().strip()

T = int(rl())

for tcase in range(1, T + 1):
    rl()
    ns = map(int, rl().split())
    n = len(ns)
    stg1 = sum([ns[i - 1] - ns[i] for i in range(1, n) if ns[i - 1] > ns[i]])
    stg2 = 0
    r = 0.0
    ns = [i * 10 for i in ns]
    for i in range(1, n):
        if ns[i] < ns[i - 1]:
            least = ns[i - 1] - ns[i]
            if r * 10.0 >= least:
                continue
            r = least / 10.0
    for i in range(n - 1):
        stg2 += min(r * 10, ns[i])

    print 'Case #%d: %d %d' % (tcase, stg1, stg2 / 10)
