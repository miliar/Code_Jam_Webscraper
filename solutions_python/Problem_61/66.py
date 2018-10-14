from scipy.misc.common import comb

D = 100003

T = int(raw_input())
for t in range(T):
    n = int(raw_input())
    ways = [[0] * n for i in range(n + 1)]
    for i in range(2, n + 1):
        ways[i][1] = 1
        for r in range(2, i):
            ways[i][r] = sum(ways[r][j] * int(round(comb(i - r - 1, r - j - 1)))
                             for j in range(2 * r - i, r))
    print 'Case #{0}: {1}'.format(t + 1, sum(ways[n]) % D)
