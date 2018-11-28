#!/usr/bin/env python

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
T = int(raw_input())  # read a line with a single integer
for t in xrange(1, T + 1):
    n, k = raw_input().split(" ")
    n = int(n)
    k = int(k)

    curr = 0
    large = n
    count = 1
    maxx = 0
    minn = 0
    step = 1
    while True:
        if curr + step >= k:
            prob = large
            if k - curr > count:
                prob = large - 1
            maxx = prob / 2
            if prob % 2 == 0:
                minn = maxx - 1
            else:
                minn = maxx
            break

        if large % 2 == 1:
            count = step + count
        large = large / 2
        curr = curr + step
        step = step * 2


    print "Case #{}: {} {}".format(t, maxx, minn)
