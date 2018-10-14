#!/usr/bin/python

# base income
B = 2.0

T = int(raw_input())
for t in range(1, T+1):
    C, F, X = (float(s) for s in raw_input().split())

    prevBuildTime = 0.0
    prevTime = X / B

    n = 1
    while True:
        buildTime = prevBuildTime + C / (B + (n-1) * F)
        time = buildTime + X / (B + n * F)
        if time >= prevTime:
            break
        prevBuildTime = buildTime
        prevTime = time
        n += 1

    print "Case #{t}: {time}".format(t=t, time=prevTime)
