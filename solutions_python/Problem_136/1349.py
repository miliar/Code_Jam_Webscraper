#!/usr/bin/env pypy

def solve(C, F, X):
    rate = 2.0
    start_time = 0
    earliest_intersect = X # 
    intersect = intersect_time(rate, start_time, X)
    while intersect < earliest_intersect:
    #    print "got here"
        earliest_intersect = intersect
        start_time = start_time + C / rate
        rate = rate + F
        intersect = intersect_time(rate, start_time, X)
    #    print "st=%s, r=%s, i = %s, ei = %s" % (start_time,rate, intersect, earliest_intersect)
    return earliest_intersect
    
    
def intersect_time(rate, start_time, X):
    i = start_time + ( X / rate )
    return i   


T = int(raw_input())
for i in range(T):
    sol = solve(*[float(x) for x in raw_input().split()]);
    print "Case #%s: %s" % (i+1, sol)

    
