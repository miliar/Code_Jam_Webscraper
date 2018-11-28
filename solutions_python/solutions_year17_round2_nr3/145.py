import math 

T = int(input())

for t in range(1, T+1):
    n, q = map(int, input().split())
    
    horse = [tuple(map(int, input().split())) for _ in range(n)]

    matrix = [list(map(int, input().split())) for _ in range(n)]

    dist = [matrix[i][i+1] for i in range(n-1)] + [0]

    dp = [math.inf for _ in range(n)]
    dp[0] = 0

    for i in range(n):
        for j in range(n-1):
            dd = sum(dist[j:i])
            if dd > horse[j][0]: continue
            dp[i] = min(dp[i], dp[j] + dd/horse[j][1])
        
    u, v = map(int, input().split())

    print("Case #%d:" % t, dp[n-1])
