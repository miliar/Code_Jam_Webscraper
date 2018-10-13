#!/usr/bin/env python

def catchup_dist(s1, s2, d):
    s_diff = s1-s2
    hours = float(d) / s_diff
    return hours * s1

def catchup_speed(s, k, d):
    d_diff = d - k
    hours = float(d_diff) / s
    return float(d) / hours

t = int(raw_input())
for i in xrange(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]
    horses = []
    for j in xrange(n):
        k, s = [int(s) for s in raw_input().split(" ")]
        horses.append((k,s))
    horses.sort(key=lambda tup: tup[0])

    new_horses = []
    curr_horse = None
    while len(horses) > 0:
        next_horse = horses.pop(0)
        if not curr_horse:
            curr_horse = next_horse
        else:
            k1, s1 = curr_horse
            k2, s2 = next_horse
            if s2 >= s1:
                continue
            c_dist = catchup_dist(s1, s2, k2-k1)
            if k1 + c_dist >= d:
                continue
            else:
                new_horses.append(curr_horse)
                curr_horse = next_horse
    new_horses.append(curr_horse)
    
    max_speed = 99999999999999
    for k1, s1 in new_horses:
        speed = catchup_speed(s1, k1, d)
        if speed < max_speed:
            max_speed = speed

    print "Case #%d: %.6f" % (i, max_speed)
