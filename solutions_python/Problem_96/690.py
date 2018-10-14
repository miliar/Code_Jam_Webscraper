max_score = [ [0,0] for i in xrange(31) ]

for i in xrange(11):
    for j in xrange(i,i+3):
        if j>10 : break
        for k in xrange(j,i+3):
            if k>10: break
            assert i<=j<=k and i+2>=j and i+2>=k
            imp = i+2==k
            max_score[i+j+k][imp] = max(max_score[i+j+k][imp], k)


def solve(score, S,P):
    N = len(score)
    INF = 1000000
    dp = [ [0]*(S+1) for i in xrange(N) ]

    dp[0][0] = int(max_score[score[0]][0]>=P)
    if S>0 : dp[0][1] = int(max_score[score[0]][1]>=P)
    for i in xrange(1,N):
        for j in xrange(0,S+1):
            dp[i][j]=dp[i-1][j] + int(max_score[score[i]][0]>=P)
            if j>0 :
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + int(max_score[score[i]][1]>=P))

    #for row in dp: print row
    return dp[N-1][S]

    

for caseid in xrange(1,int(raw_input())+1):
    data = map(int, raw_input().split())
    N, S, P = data[:3]
    scores = data[3:3+N]
    print "Case #%d: %d"%(caseid, solve(scores, S, P))


