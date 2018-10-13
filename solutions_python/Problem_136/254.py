#!/usr/bin/env python

def cookie(cost, rate_bump, total):
    cur_time = 0.0
    cur_rate = 2.0
    min_end = total / cur_rate
    while True:
        cur_time += cost / cur_rate
        cur_rate += rate_bump
        new_end = cur_time + total / cur_rate
        if (new_end > min_end):
            return min_end
        else:
            min_end = new_end

for case in xrange(1, int(raw_input())+1):
    cost, rate_bump, total = map(float, raw_input().split())
    print "Case #%d: %f" % (case, cookie(cost, rate_bump, total))
