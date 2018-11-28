from __future__ import division


def calc_horse_time(distance_left, speed):
    return distance_left / speed

t = int(raw_input())

for i in xrange(1, t+1):
    d, n = map(int, raw_input().split())
    slowest_time = 0

    for _ in xrange(n):
        k, s = map(int, raw_input().split())
        slowest_time = max(slowest_time, calc_horse_time(d - k, s))

    print "Case #{}: {}".format(i, d / slowest_time)
