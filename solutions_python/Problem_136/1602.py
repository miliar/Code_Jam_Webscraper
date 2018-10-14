import sys
getint = lambda: int(raw_input())
getfloats = lambda: [float(z) for z in raw_input().split()]

def timewait(nc, cps, X):
    return (float(X) - float(nc)) / float(cps)

def timeforfarm(nc, cps, C):
    return (float(C) - float(nc))  / float(cps)

assert timeforfarm(0, 2, 30) == 15.0

for t in xrange(1, 1+getint()):
    C,F,X = getfloats()
    # C cost of a farm
    # F cookies per second of the farm
    # X destination nr of cookies
    nc = 0
    cps = 2
    time = 0.0

    while 1:
        w1 = timewait(nc, cps, X)
        f = timeforfarm(nc, cps, C)
        w2 = f + timewait(nc, cps + F, X)

        if w1 <  w2 :
            time += w1
            break
        else:
            time += f
            nc -= C
            nc += cps * f
            cps += F

    print "Case #%d: %.10f" % (t, time)
