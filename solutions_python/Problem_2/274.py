#!/usr/bin/python2.5
# Solution to Google Code Jam 08 Problem B
# Matt Giuca

# Usage: ./probB.py < inputfile > outputfile

# Note: Station "A" and "B" are referred to as 0 and 1 respectively.

import sys

DEBUG = False

class Time(object):
    """
    A time in HH:MM.
    """
    def __init__(self, h, m):
        self.h = h
        self.m = m
    def __repr__(self):
        return "Time(%r, %r)" % (self.h, self.m)
    def __str__(self):
        return "%02d:%02d" % (self.h, self.m)
    def __eq__(self, other):
        return self.h == other.h and self.m == other.m
    def __cmp__(self, other):
        return cmp((self.h, self.m), (other.h, other.m))
    def __hash__(self):
        return hash((self.h, self.m))
    @staticmethod
    def parse(hhmm):
        return Time(*map(int, hhmm.split(':')))
    def __add__(self, other):
        """
        other: int (minutes)
        """
        newM = self.m + other
        return Time(self.h + (newM // 60), newM % 60)

class Event(object):
    """
    Some event (abstract type).
    """
    def __init__(self, platform, time):
        self.platform = platform
        self.time = time
    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__,
                               self.platform, self.time)
    def __eq__(self, other):
        return self.__class__ == other.__class__ and \
                self.platform == other.platform and \
                self.time == other.time
    def __hash__(self):
        return hash((self.__class__, self.platform, self.time))

class Arrive(Event):
    """
    An arrival event.
    """
    pass

class Depart(Event):
    """
    A departure event.
    """
    pass

def insert_sorted(lst, val, key=lambda x: x):
    for i in range(len(lst)):
        if key(val) < key(lst[i]):
            lst.insert(i, val)
            return
    lst.append(val)

def parse(file=sys.stdin):
    """
    (Generator) Read input file from filename or file or stdin.
    Yields lists of events (one per case).
    Automatically accounts for turnaround time (adds it to arrival time).
    """
    if isinstance(file, basestring):
        file = open(file)
        toclose = True
    else:
        toclose = False
    n = int(file.readline().strip())
    for i in range(n):
        events = []     # List of Events, sorted by time
        t = int(file.readline().strip())        # Turnaround time (mins)
        na, nb = map(int, file.readline().strip().split())
        for j in range(na):
            parse_trip(file, t, 0, 1, events)
        for j in range(nb):
            parse_trip(file, t, 1, 0, events)
        yield events

    if toclose:
        file.close()

def parse_trip(file, t, depart_plat, arrive_plat, events):
    """
    Parses a trip in a file. Reads one line.
    t: int. Turnaround time (mins).
    depart_plat, arrive_plat: int. Platform of arrival, departure.
    Updates events dict. Automatically accounts for turnaround time.
    """
    depart_time, arrive_time = map(Time.parse,
                                   file.readline().strip().split())
    arrive_time += t        # Add turnaround time to arrival time
    def sortkey(event):
        # Sort first by time, then put arrivals before departures
        # (So a train arriving can leave immediately)
        return (event.time, isinstance(event, Depart))
    insert_sorted(events, Depart(depart_plat, depart_time), key=sortkey)
    insert_sorted(events, Arrive(arrive_plat, arrive_time), key=sortkey)

def solve_case(events):
    """
    Given a list of Events, returns an (int, int) pair; the number of trains
    that need to start at platforms 0 and 1 respectively.
    """
    # Simulate the train system, and if we find we need a train where we don't
    # have one, increase the start count for that platform.
    # Indices of these lists are platform numbers (0 and 1).
    start_trains = [0, 0]
    cur_trains = [0, 0]
    for event in events:
        if isinstance(event, Arrive):
            cur_trains[event.platform] += 1
            if DEBUG:
                print event.time, "Arrival at Platform", event.platform
                print "    Stock: %d, %d" % (cur_trains[0], cur_trains[1])
        elif isinstance(event, Depart):
            if DEBUG:
                print event.time, "Departure from Platform", event.platform
            if cur_trains[event.platform] == 0:
                if DEBUG:
                    print "    Need to order another train at platform", \
                          event.platform
                start_trains[event.platform] += 1
            else:
                cur_trains[event.platform] -= 1
            if DEBUG:
                print "    Stock: %d, %d" % (cur_trains[0], cur_trains[1])
    return tuple(start_trains)

def do_all(file=sys.stdin):
    """
    Processes input, prints output to stdout.
    """
    i = 0
    for events in parse(file):
        i += 1
        sa, sb = solve_case(events)
        print("Case #%d: %d %d" % (i, sa, sb))

if __name__ == "__main__":
    do_all()
