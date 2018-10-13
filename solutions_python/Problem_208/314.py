

N = 0
Q = 0
def calc():
    global N, Q
    N, Q = map(int, raw_input().split())
    horses = []
    adj = []    
    paths = []
    for b_i in xrange(N):
        horses.append(map(float, raw_input().split()))
    for b_i in xrange(N):
        adj.append(map(float, raw_input().split()))
    for b_i in xrange(Q):
        paths.append(map(int, raw_input().split()))
    dp = []
    for x in xrange(N):
        dp.append([0]*N)
        for y in xrange(N):
            dp[x][y] = [float('inf'), float('inf')]
    dp[0][0] = [0.0, horses[0][0]]
    for i in xrange(1, N):
        mn = float('inf')
        for j in xrange(i):
            r = dp[j][i-1][1]
            dist = adj[i-1][i]
            if r >= dist:
                t =  dp[j][i-1][0] + dist/horses[j][1]
                dp[j][i] = [t, r - dist]
            else:
                continue
            if t < mn:
                mn = t
        dp[i][i] = [mn, horses[i][0]]
        # print dp[N-1]
    return dp[N-1][N-1][0]

T = int(raw_input())

for a_i in xrange(T):

    ans = "Case #{}: {}".format(a_i+1, calc())
    print ans
