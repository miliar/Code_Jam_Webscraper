from copy import copy

IN = open('input.txt', 'r')

T = int(IN.readline())

dp = [[0 for i in xrange(1 << 20)] for j in xrange(2)]

for ttt in xrange(1, T + 1):

    N = int(IN.readline())
    L = map(int, IN.readline().strip().split())
    for i in xrange(1 << 20):
        dp[0][i] = 0

    bound = 0
    Max = 0
    Sum = 0
    x = 0    

    for w in L:
        Sum ^= w
        x ^= 1
        dp[x] = copy(dp[x ^ 1])
        for i in xrange(bound + 1):
            if i == 0 or dp[x ^ 1][i] > 0:
                dp[x][i ^ w] = max(dp[x][i ^ w], dp[x ^ 1][i] + w)
            bound = max(bound, i ^ w)

    for i in xrange(1, bound + 1):
        if Sum ^ i == i:
            Max = max(Max, dp[x][i])

    print 'Case #{}:'.format(ttt),

    if Max == 0:
        print 'NO'
    else:
        print Max
