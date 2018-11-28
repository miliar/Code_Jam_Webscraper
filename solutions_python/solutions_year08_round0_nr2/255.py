#!/usr/bin/env python

from sys import stdin

n = int(stdin.readline())

E_READY = 0
E_DEP = 1

def read_events(src_list, dst_list, num):
    for i in xrange(num):
        dep,arr = [[int(i) for i in time.split(':')] for time in
                      stdin.readline().split(' ')]
        dep = dep[0]*60 + dep[1]
        arr = arr[0]*60 + arr[1]

        src_list.append((dep, E_DEP))
        dst_list.append((arr+t, E_READY))

def count_trains(elist):
    ret = 0
    avail = 0
    for (time, tp) in elist:
        if tp == E_DEP:
            if avail > 0:
                avail -= 1
            else:
                ret += 1
        else:
            avail += 1
    return ret

for case in xrange(n):
    t = int(stdin.readline())
    (na,nb) = [int(i) for i in stdin.readline().split(' ')]
    
    a_events = []
    b_events = []

    read_events(a_events, b_events, na)
    read_events(b_events, a_events, nb)

    a_events.sort()
    b_events.sort()

    a_count = count_trains(a_events)
    b_count = count_trains(b_events)

    print 'Case #%d: %d %d' % (case+1, a_count, b_count)
