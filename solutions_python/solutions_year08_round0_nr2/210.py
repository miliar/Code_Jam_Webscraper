#!/usr/bin/env python

import sys
f=sys.stdin
n=int(f.next())

class Event(tuple):
    DEP="dep"
    ARR="arr"
    def __init__(self, arg):
        self.time, self.type, self.station = self

def get_trip(dep_station, arr_station):
    def to_minutes(s):
        h,m = map(int, s.split(':'))
        return h*60+m
    dep,arr = map(to_minutes, f.next().split())
    return (dep, Event.DEP, dep_station), (arr+tt, Event.ARR, arr_station)

for case in xrange(1,n+1):
    # Read case into a list of events
    tt = int(f.next())
    ntrips_per_station = map(int, f.next().split())
    trains_required = {}
    trains_available = {}
    events = []
    for station, ntrips in enumerate(ntrips_per_station): 
        src, dst = ["AB","BA"][station]
        trains_required[src] = 0
        trains_available[src] = 0
        for i in range(ntrips):
            trip = get_trip(src, dst)
            events.append(Event(trip[0]))
            events.append(Event(trip[1]))
    events.sort()

    for ev in events:
        if ev.type is Event.DEP:
            if trains_available[ev.station]:
                trains_available[ev.station]-=1
            else:
                trains_required[ev.station]+=1
        elif ev.type is Event.ARR:
            trains_available[ev.station]+=1


    print "Case #%s: %s %s"%(case, trains_required['A'], trains_required['B'])
