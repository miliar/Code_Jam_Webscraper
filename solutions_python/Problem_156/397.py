__author__ = 'zumzoom'


if __name__ == '__main__':
    with open('input.txt') as inf:
        with open('output.txt', 'w') as of:
            MAXN = 1005
            MAXJ = 40
            INF = 10000000
            # dp = [[INF for __ in range(MAXJ)] for _ in range(MAXN)]
            # dp[0] = [0 for __ in range(MAXJ)]
            # for i in range(1, MAXN):
            #     for j in range(0, MAXJ):
            #         dp[i][j] = dp[i-1][j] + 1
            #         for q in range(1, i):
            #             dp[i][j] = min(dp[i][j], max(dp[i-q][j-1], dp[q][j-1]) + 1)

            t = int(inf.readline())
            for k in range(t):
                n = int(inf.readline())
                p = [int(x) for x in inf.readline().split()]
                ans = INF
                for i in range(1, MAXN):
                    splt = 0
                    for pt in p:
                        splt += pt // i
                        if pt % i == 0:
                           splt -= 1
                    ans = min(ans, splt + i)

                of.write("Case #{}: {}\n".format(k + 1, ans))
