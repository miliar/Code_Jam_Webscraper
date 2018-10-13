def solve():
    C, F, X = map(float, raw_input().split(" "))
    seconds = 0
    currentC = 0
    per = 2
    buf = []
    min = X / 2;
    while True:

        if min < seconds + C / per + X / (per + F):
            return min
        seconds += C / per
        per += F
        min = seconds+X / per


T = int(raw_input())
for t in xrange(1, T + 1):
    print "Case #%d: %s" % (t, solve())
