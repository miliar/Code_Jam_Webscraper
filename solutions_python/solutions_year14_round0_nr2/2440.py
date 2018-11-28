from heapq import heappush, heappop

cases = int(raw_input())

for c in xrange(cases):
    C, F, X = map(float, raw_input().split(" "))

    base_rate = 2.0
    tmax =  X / base_rate
    best = tmax
    t = 0.0
    rate = base_rate
    while True:
        t = t + (C / rate)
        rate += F
        potential =  t + (X/rate)
        if potential <= best:
            best = potential
        else:
            break
        best =  min(best, t + (X/rate))

    print "Case #%d: %.7f" % (c+1, best)

