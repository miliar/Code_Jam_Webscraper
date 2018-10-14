T = int(raw_input())

def wp(s):
    wins = 0.0
    games = 0.0
    for c in s:
        if c != '.':
            games += 1.0
        if c == '1':
            wins += 1.0
    return wins/games


for case in xrange(1, T+1):
    N = int(raw_input())

    grid = []
    for i in xrange(N):
        grid.append(raw_input().strip())

    WP = []
    for i in xrange(N):
        WP.append(wp(grid[i]))

    OWP = []
    for i in xrange(N):
        numops = 0.0
        temp = 0.0
        for j in xrange(N):
            if i == j or grid[i][j] == '.':
                continue
            temp += wp(grid[j][:i] + grid[j][i+1:])
            numops += 1.0
        OWP.append(temp/numops)

    OOWP = []
    for i in xrange(N):
        numops = 0.0
        temp = 0.0
        for j in xrange(N):
            if i == j or grid[i][j] == '.':
                continue
            temp += OWP[j]
            numops += 1.0
        OOWP.append(temp/numops)

    print "Case #%d:"%case
    for i in xrange(N):
        print 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]



