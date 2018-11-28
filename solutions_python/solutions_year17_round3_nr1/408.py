import math

PI = math.pi

def f(p):
    return 2*PI*p[0]*p[1]

T = int(input())
for test in range(1, T+1):
    N, K = [int(x) for x in input().strip().split(' ')]
    pancakes = []
    for _ in range(N):
        r, h = [int(x) for x in input().strip().split(' ')]
        pancakes.append([r, h])
    pancakes.sort(reverse=True)
    dp = [[0]*(N+1) for _ in range(N+1)]
    prev = 0
    for i in range(1, N+1):
        dp[i][1] = max(prev, 2*PI*pancakes[i-1][0]*pancakes[i-1][1] + PI*pancakes[i-1][0]*pancakes[i-1][0])
        prev = dp[i][1]

    for i in range(2, N+1):
        for j in range(2, min(i+1, K+1)):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+2*PI*pancakes[i-1][0]*pancakes[i-1][1])
    r = dp[N][K]
    print('Case #%d: %.9f' % (test, r))