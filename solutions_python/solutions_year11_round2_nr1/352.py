import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    score = [sys.stdin.readline().strip() for n in range(N)]

    # Sum up all of the wins
    wins = [0.0] * N
    played = [0.0] * N
    for team in range(N):
        for opponent in range(N):
            if score[team][opponent] == '1':
                wins[team] += 1
                played[team] += 1
            elif score[team][opponent] == '0':
                played[team] += 1

    WP = [ wins[n] / played[n] for n in range(N) ]

    def owp(n):
        s = 0
        for op in range(N):
            if score[n][op] == '1' :
                s += (wins[op] - 0) / (played[op] - 1)
            elif score[n][op] == '0':
                s += (wins[op] - 1) / (played[op] - 1)
        return s
    OWP = [ owp(n) / played[n] for n in range(N) ]

    def oowp(n):
        s = 0
        for op in range(N):
            if score[n][op] != '.':
                s += OWP[op]
        return s
    OOWP = [ oowp(n) / played[n] for n in range(N) ]

    def rpi(n):
        return 0.25 * WP[n] + 0.5 * OWP[n] + 0.25 * OOWP[n]
    
    RPI = [rpi(n) for n in range(N)]
    print 'Case #%d:' % (t + 1)
    for rpi in RPI:
        print rpi

