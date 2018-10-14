import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

(T,) = read_nums()
for test in range(1, T+1):
    (X, S, R, t, N) = read_nums()
    total_len = 0
    walkways = []
    for n in range(N):
        (B, E, w) = read_nums()
        total_len += E - B
        walkways.append( (w, E - B) )
    walkways.append( (0, X - total_len) )
    walkways.sort()
    time = 0.0
    for walkway in walkways:
        w = walkway[0]
        width = walkway[1]
        run_time = min(t, 1.0 * width / (w+R))
        walk_time = float(width - run_time*(w+R)) / (w+S)
        t -= run_time
        time += run_time + walk_time
    print "Case #%d: %.9f" % (test, time)

