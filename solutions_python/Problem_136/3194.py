#farms = 0
#f = 0
#rate = 2 * nfarms * F
def best(r, s, C, F, X):
    while 1:
        t0 = X/r
        t1 = C/r + X/(F+r)
        if t0 <= t1:
            return s + t0

        s += C/r
        r += F

T = int(input())
for case in range(T):
    C, F, X = [float(f) for f  in input().split(' ')]
    print ("Case #%s: %.7f" % (case+1, best(2, 0, C, F, X)))
