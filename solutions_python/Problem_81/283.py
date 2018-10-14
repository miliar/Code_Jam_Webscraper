# Google Code Jam : Round 1B 2011 : Problem A. RPI
# https://code.google.com/codejam/contest/dashboard?c=1150485#s=p0
# Python 2.6.5

def solve_case(t, games):
    N = len(games)

    WP = {}
    for i in range(N):
        s = 0
        num = 0
        
        for j in range(N):
            
            c = games[i][j]
            
            if c == '0':
                num += 1
            if c == '1':
                num += 1
                s += 1

        WP[i] = 1.0 * s / num


    preOWP = {}
    for i in range(N):
        preOWP[i] = {}

        for j in range(N):
            if i == j:
                continue

            if games[i][j] == '.':
                continue

            s = 0
            num = 0
            
            for k in range(N):
                
                if k == i:
                    continue

                c = games[j][k]
            
                if c == '0':
                    num += 1
                if c == '1':
                    num += 1
                    s += 1

            preOWP[i][j] = 1.0 * s / num
    
    OWP = {}
    for i in range(N):
        OWP[i] = 1.0 * sum(preOWP[i].itervalues()) / len(preOWP[i])

    OOWP = {}
    for i in range(N):
        s = 0
        num = 0

        for j in range(N):
            if i == j:
                continue

            if games[i][j] == '.':
                continue

            s += OWP[j]
            num += 1

        OOWP[i] = 1.0 * s / num

    print "Case #" + str(t) + ":"
    for i in range(N):
        RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]
        print RPI


def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        games = []
        for i in range(N):
            games.append(raw_input().strip())
        solve_case(t, games)

solve()
