#!/usr/bin/python

tc = int(raw_input())
for t in range(0, tc):
    c, f, x = map(float, raw_input().split(' '))
    speed = 2.0

    farms = 0
    result = float("inf")
    current = x / speed
    last = current

    while current < result:
        result = current

        current -= last
        current += c / speed
        last = x / (speed + f)
        current += last
        speed += f

    print "Case #%s: %s" % (t + 1, result)
