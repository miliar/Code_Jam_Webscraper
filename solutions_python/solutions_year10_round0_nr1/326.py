#!/usr/bin/python

for case in range(input()):
    N, K = map(int, raw_input().split())
    on = ((2 ** N - 1) & K) == (2 ** N - 1)
    print "Case #%s: %s" % (case + 1, "ON" if on else "OFF")
