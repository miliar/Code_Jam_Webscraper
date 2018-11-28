import sys

def next_line():
    return input_file.readline().rstrip()

DIST, SPEED, TIME = 0, 1, 2

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N, Q = map(int, next_line().split())
    ponies = []
    for i in xrange(N):
        ponies.append(map(int, next_line().split()))
    dist = []
    for i in xrange(N):
        dist.append(map(int, next_line().split()))
    for i in xrange(Q):
        start, end = map(int, next_line().split())

    #print ponies
    current = [ponies[0] + [0]]
    for i, pony in enumerate(ponies):
        if i == 0:
            continue
        d = dist[i-1][i]
        assert(d >= 0)
        min_time = float("inf")
        new = []
        for cp in current:
            if cp[DIST] < d:
                continue
            t = float(d) / cp[SPEED]
            cp[TIME] += t
            cp[DIST] -= d
            min_time = min(min_time, cp[TIME])
            new.append(cp)
        if min_time == float("inf"):
            print "IMPOSSIBLE"
            break
        new.append(pony + [min_time])
        current = new
        #print current
    print min_time
