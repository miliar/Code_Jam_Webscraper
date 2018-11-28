def solve():
    N, M = map(int , raw_input().split())
    lawn = [map(int , raw_input().split()) for i in xrange(N)]
    cut_table = [[False] * M for i in xrange(N)]
    for j in xrange(M):
        max_height = 0
        for i in xrange(N):
            max_height = max(max_height, lawn[i][j])
        for i in xrange(N):
            if lawn[i][j] == max_height:
                cut_table[i][j] = True
    for i in xrange(N):
        max_height = max(lawn[i])
        for j in xrange(M):
            if lawn[i][j] == max_height:
                cut_table[i][j] = True
        if False in cut_table[i]:
            return "NO"
    return "YES"

T = int(raw_input())
for i in xrange(T):
    print "Case #%d:" % (i + 1), solve()
