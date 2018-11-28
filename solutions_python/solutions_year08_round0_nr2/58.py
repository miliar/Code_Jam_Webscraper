#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Scott Patterson
# asp742@gmail.com
#

import sys
from itertools import cycle

def time2min(t):
    hour, min = [int(x) for x in t.split(':')]
    
    return hour*60 + min

def get_trains(RA, RB, T):
    RA.sort()
    RB.sort()

    station_data = {'A': {'num': 0, 'routes': RA},
                    'B': {'num': 0, 'routes': RB}}

    station_cycle = cycle(station_data.values())

    while len(RA) > 0 and len(RB) > 0:

        # find earliest route
        route = station_cycle.next()['routes'][0]
        if route > station_cycle.next()['routes'][0]:
            station_cycle.next()

        # add a train for earliest route
        station = station_cycle.next()
        route = station['routes'].pop(0)
        train_free = route[1] + T
        station['num'] += 1

        # find connection trip segment else start new train
        for next_station in station_cycle:
            next_leg = None
            for r in next_station['routes']:
                if r[0] >= train_free:
                    next_leg = r
                    break

            # no more connecting routes for this train
            if not next_leg:
                break
            
            # otherwise add a connecting route to this train
            station = next_station
            station['routes'].remove(r)
            route = r   
            train_free = route[1] + T

    # Add remaining routes
    num_A = station_data['A']['num'] + len(RA)
    num_B = station_data['B']['num'] + len(RB)

    return num_A, num_B

def main():
    file = sys.argv[1]
    data = (lines.strip() for lines in open(file))

    ncase = int(data.next())
    for case in range(ncase):
        T = int(data.next())
        NA, NB = [int(x) for x in data.next().split()]
        RA = []
        RB = []
        for n, route_list in ((NA, RA), (NB, RB)):
            for r in range(n):
                route_list.append(tuple(time2min(t) for t in data.next().split()))

        num_A, num_B = get_trains(RA, RB, T)

        print 'Case #%d: %d %d' % (case+1, num_A, num_B)

if __name__ == '__main__':
    main()
