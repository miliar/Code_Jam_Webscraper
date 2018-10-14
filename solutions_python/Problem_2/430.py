#!/usr/bin/env python

from sys import argv
import string

def trains(trips_a_b, trips_b_a, turn_time):
    trips_a_b.sort()
    trips_b_a.sort()
    
    a_trains, b_trains = 0, 0
    a_used, b_used = list(trips_a_b), list(trips_b_a)    
    cmpr = lambda x, y: cmp(x[1], y[1])
    a_used.sort(cmpr)
    b_used.sort(cmpr)
    
    for trip in trips_a_b:
        a_trains += 1
        for d, a in b_used:
            if trip[0] >= (a + turn_time):
                a_trains -= 1
                b_used = b_used[1:]
                break
            
    for trip in trips_b_a:
        b_trains += 1
        for d, a in a_used:
            if trip[0] >= (a + turn_time):
                b_trains -= 1
                a_used = a_used[1:]
                break
                
    return a_trains, b_trains

f = open(argv[1], "rb")
num_cases = int(f.readline())
for case in xrange(num_cases):
    turn_time = int(f.readline())
    num_trips_a_b, num_trips_b_a = map(int, f.readline().split())
    trips_a_b, trips_b_a = [], []
    for trip_num in xrange(num_trips_a_b):
        trips_a_b.append(map(int, map(lambda x: x.replace(":", ""), f.readline().split())))
    for trip_num in xrange(num_trips_b_a):
        trips_b_a.append(map(int, map(lambda x: x.replace(":", ""), f.readline().split())))
    r1, r2 = trains(trips_a_b, trips_b_a, turn_time)
    print "Case #%d: %d %d" % (case + 1, r1, r2)
