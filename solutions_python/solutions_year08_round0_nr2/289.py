#!/usr/bin/env python

#---------------------------------------------------------------------------
# Google Code Jam 2008
#
# Gavin Baker <gavinb@antonym.org>
#
# Qualification Round
# B: Train Timetable
#---------------------------------------------------------------------------

import sys
import datetime
import logging

ARRIVE = 1
DEPART = -1
STATION_A = 1
STATION_B = 2
ARRDEP = {ARRIVE: 'Arrive', DEPART: 'Depart'}
STATION = {STATION_A: 'Station_A', STATION_B: 'Station_B'}

#---------------------------------------------------------------------------

def parse_time(ts):
    h,m = map(int, ts.split(':'))
    return datetime.datetime(2008,1,1,h,m)

def cmp_event_time(x, y):
    dep_x, deparr_x, stn_x = x
    dep_y, deparr_y, stn_y = y
    # For the same time, handle arrivals before departures
    if dep_x == dep_y:
        if deparr_x > deparr_y:
            return -1
        elif deparr_x == deparr_y:
            return 0
        else:
            return 1
    elif dep_x < dep_y:
        return -1
    else:
        return 1

#---------------------------------------------------------------------------

def solve(infile):

    # Turnaround time
    T = datetime.timedelta(minutes=int(infile.readline()))
    logging.info('Turnaround time: %s' % T)

    # Number of trips
    NA, NB = map(int, infile.readline().split())
    logging.info('Trips: A>B: %u, B>A: %u' % (NA, NB))

    # Schedule of events - arrival times include turnaround
    timetable = []

    # Read schedule from A-B
    for i in range(0, NA):
        dep, arr = map(parse_time, infile.readline().split())
        logging.info('A>B: %s, %s' % (dep, arr))
        timetable.append((dep,   DEPART, STATION_A))
        timetable.append((arr+T, ARRIVE, STATION_B))

    # Read schedule from B-A
    for i in range(0, NB):
        dep, arr = map(parse_time, infile.readline().split())
        logging.info('B>A: %s, %s' % (dep, arr))
        timetable.append((dep,   DEPART, STATION_B))
        timetable.append((arr+T, ARRIVE, STATION_A))

    # Run the schedule, tracking how many trains are needed
    trains = {STATION_A: 0, STATION_B: 0}
    trains_needed = {STATION_A: 0, STATION_B: 0}
    timetable.sort(cmp_event_time)

    for time, arrdep, station in timetable:
        logging.info('%s Train %ss %s' % (time,ARRDEP[arrdep],STATION[station]))
        trains[station] += arrdep
        trains_needed[station] = min(trains[station], trains_needed[station])
        logging.info('Needed: %s' % trains_needed)

    #
    return "%u %u" % (-trains_needed[STATION_A], -trains_needed[STATION_B])

#---------------------------------------------------------------------------

def process(infile):

    # Number of cases
    N = int(infile.readline())

    for case_num in range(0, N):
        result = solve(infile)
        print 'Case #%u: %s' % (case_num+1, result)

if __name__=='__main__':
    if len(sys.argv) > 1:
        logging.basicConfig(level=logging.DEBUG)
    process(sys.stdin)
