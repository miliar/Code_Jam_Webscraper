T = int(raw_input())
for qq in xrange(1,T+1):
    N,M = map(int,raw_input().split(" "))
    lawn = [map(int,raw_input().split(" ")) for x in xrange(N)]
    rows = [-1000] * N
    cols = [-1000] * M
    ans = "YES"
    for x in xrange(N):
        for y in xrange(M):
            rows[x] = max(rows[x], lawn[x][y])
            cols[y] = max(cols[y], lawn[x][y])
    for x in xrange(N):
        for y in xrange(M):
            if lawn[x][y] < min(rows[x], cols[y]):
                ans = "NO"
    print "Case #%d: %s"%(qq,ans)
