#! /usr/bin/env python

T = int(raw_input())
t = 1
while t <= T:
    C, F, X = map(float, raw_input().split())

    minTime = X/2.0
    time = 0
    cookies = 0
    rate = 2.0
    while True:
        t1 = time + (X-cookies)/rate

        time += C/rate
        rate += F
        t2 = X/rate + time

        mt = min(t1, t2)
        if mt < minTime:
            minTime = mt
        else:
            break

    print "Case #%s: %s" % (t, minTime)
    t += 1
