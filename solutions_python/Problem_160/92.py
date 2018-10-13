from math import pow
CA = input()

M = long(pow(10, 14))

def served(t, m):
    return sum(t / c for c in m)

def solve(tc):
    B, N = map(int, raw_input().split())
    m = map(int, raw_input().split())
    if N <= B:
        return N
    N -= B
    # print B, m
    lo, hi = 0, M
    mt = min(m)
    while hi - lo > mt:
        x = (lo + hi) / 2
        at_x = served(x, m)
        if at_x >= N:
            hi = x
        else:
            lo = x
    # print lo, hi
    # print N, served(lo, m), served(hi, m)
    for i in range(lo, hi):
        x, y = served(i, m), served(i + 1, m)
        if x < N <= y:
            # print i, x, y, N
            return [j for j, c in enumerate(m) if (i + 1) % c == 0][N - x - 1] + 1
            break
    return 0


for tc in range(1, CA + 1):
    print "Case #%d: %s" % (tc, solve(tc))
