# -*- coding: utf-8 -*-

import time

def time2float(t):
    """xx:xx to a 1970/1/1 unix timestamp"""
    tuple = (1970, 1, 1, int(t[0:2]), int(t[3:5]), 0, 0, 1,-1)
    return time.mktime(tuple)

def sumAndThink(events):
    """
    Given a list of events (time, trainOffset),
    computes the number of trains needed at the start of the
    day to have enough trains for each event
    """
    sum = {}
    for (time, offset) in events:
        try:
            old = sum[time]
        except KeyError:
            old = 0
        sum[time] = old + offset

    events = sum.items()
    events.sort()

    trains = 0
    min = 0
    for (time, offset) in events:
        trains += offset
        if trains < min:
            min = trains
    return -min
    
f = open('input', 'r')
lines = f.readlines()
test = 1
i = 1
while i < len(lines):
    # in seconds
    turnaround = int(lines[i])*60
    i += 1

    [AB, BA] = lines[i].split()
    AB = int(AB)
    BA = int(BA)
    i += 1

    events_A = []
    events_B = []

    for line in lines[i:i+AB]:
        [d, a] = line.split()
        d = time2float(d)
        a = time2float(a)
        # make the arrival time be the arrival+turnaround time
        a = a + turnaround
        # minus one train at station A at departure d
        events_A.append((d, -1))
        # plus one train at station B at arrival+turnaround b
        events_B.append((a, 1))

    i += AB
        
    for line in lines[i:i+BA]:
        [d, a] = line.split()
        d = time2float(d)
        a = time2float(a)
        a = a + turnaround
        events_B.append((d, -1))
        events_A.append((a, 1))
    i += BA
    
    print 'Case #%s: %s %s' % (test, 
                               sumAndThink(events_A), 
                               sumAndThink(events_B))
    test += 1   
