#!/bin/env python
# -*- coding: utf-8 -*-
'''Python for Google Code Jam 2008 Qualification Round, Train Timetable

Problem

A train line has two stations on it, A and B. Trains can take trips from A to B or from B to A multiple times during a day. When a train arrives at B from A (or arrives at A from B), it needs a certain amount of time before it is ready to take the return journey - this is the turnaround time.

A train timetable specifies departure and arrival time of all trips between A and B. The train company needs to know how many trains have to start the day at A and B in order to make the timetable work: whenever a train is supposed to leave A or B, there must actually be one there ready to go. There are passing sections on the track, so trains don't necessarily arrive in the same order that they leave.

Input
The first line of input gives the number of cases, N. N test cases follow.

Each case contains a number of lines. The first line is the turnaround time, T, in minutes. The next line has two numbers on it, NA and NB. NA is the number of trips from A to B, and NB is the number of trips from B to A. Then there are NA lines giving the details of the trips from A to B.

Each line contains two fields, giving the HH:MM departure and arrival time for that trip. The departure time for each trip will be earlier than the arrival time. All arrivals and departures occur on the same day. The trips may appear in any order - they are not necessarily sorted by time. The hour and minute values are both two digits, zero-padded, and are on a 24-hour clock (00:00 through 23:59).

After these NA lines, there are NB lines giving the departure and arrival times for the trips from B to A.

Output
For each test case, output one line containing "Case #x: " followed by the number of trains that must start at A and the number of trains that must start at B.

Limits

1 ≤ N ≤ 100

Small dataset

0 ≤ NA, NB ≤ 20
0 ≤ T ≤ 5

Large dataset

0 ≤ NA, NB ≤ 100
0 ≤ T ≤ 60

Sample

Input
----
2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02
	
Output
Case #1: 2 2
Case #2: 2 0
'''

def train_timetable(inputs):
    '''Generate output for the 'Train Timetable' problem

    Example:
    >>> i = """2
    ... 5
    ... 3 2
    ... 09:00 12:00
    ... 10:00 13:00
    ... 11:00 12:30
    ... 12:02 15:00
    ... 09:00 10:30
    ... 2
    ... 2 0
    ... 09:00 09:01
    ... 12:00 12:02"""
    >>> print train_timetable(i)
    Case #1: 2 2
    Case #2: 2 0
    '''
    line = inputs.split("\n")
    l = 0

    num_cases = int(line[l])
    l+=1
    solution = []

    for c in xrange(num_cases):
        turnaround = int(line[l])
        l+=1

        timesA, timesB = [int(x) for x in line[l].split()]
        l+=1;

        timetableA = []
        for t in xrange(timesA):
            timetableA.append(line[l].split())
            l+=1
        timetableB = []
        for t in xrange(timesB):
            timetableB.append(line[l].split())
            l+=1

        solution.append(solve(turnaround, timetableA, timetableB))

    output = []
    for s, n in zip(solution, xrange(1, num_cases+1)):
        a,b = s
        output.append("Case #%d: %d %d"%(n, a, b))
    return "\n".join(output)

def solve(turnaround, timetableA, timetableB):
    '''Solve a 'Train Timetable' problem

    I got a little code happy and tried for a more general case of N stations.
    dest_station is where I had to give up the attempt.

    Example:
    >>> turnaround = 5
    >>> tta = []
    >>> tta.append(('09:00','12:00'))
    >>> tta.append(('10:00','13:00'))
    >>> tta.append(('11:00', '12:30'))
    >>> ttb = []
    >>> ttb.append(('12:02', '15:00'))
    >>> ttb.append(('09:00', '10:30'))
    >>> print solve(turnaround, tta, ttb)
    [2, 2]
    >>> turnaround = 2
    >>> tta = []
    >>> tta.append(('09:00','09:01'))
    >>> tta.append(('12:00','12:02'))
    >>> ttb = []
    >>> print solve(turnaround, tta, ttb)
    [2, 0]
    >>> turnaround = 3
    >>> tta = [('01:40','01:41')]
    >>> ttb = [('01:44','01:45')]
    >>> print solve(turnaround, tta, ttb)
    [1, 0]
    '''

    leaving = []
    leaving.append(make_schedule(timetableA))
    leaving.append(make_schedule(timetableB))
    in_transit = []
    waiting = [0] * 2
    starting = [0] * 2

    while (1):
        # Pick the station to process next
        depart_station = -1
        earliest = 24*60 + 1
        for num, l in zip(xrange(len(leaving)),leaving):
            if l:
                if l[0][0] <= earliest:
                    depart_station = num
                    earliest = l[0][0]
        # Did we run out of trains?
        if -1 == depart_station: break

        # Get the departing trains
        departure, arrivals = leaving[depart_station].pop(0)

        # Any in-transit trains arrive?
        new_in_transit = []
        for to, arrival in in_transit:
            if (arrival + turnaround) <= departure:
                waiting[to] += 1
            else: new_in_transit.append((to, arrival))
        in_transit = new_in_transit

        # For each departing train, match to a waiting train or add a new starting train
        for arrival_time in arrivals:
            if waiting[depart_station] > 0: waiting[depart_station] -= 1
            else: starting[depart_station] += 1

            if 0 == depart_station: dest_station = 1
            else: dest_station = 0

            in_transit.append((dest_station, arrival_time))

    # Return is how many needed at start of day
    return starting

def make_schedule(timetable):
    '''Take a list of departure and arrival strings and create a schedule
    
    Example:
    >>> tt = []
    >>> tt.append(('09:00','12:00'))
    >>> tt.append(('10:00','13:00'))
    >>> print make_schedule(tt)
    [(540, [720]), (600, [780])]
    '''

    leaving = dict()
    for t in timetable:
        departure_time, arrival_time = normalize_times(t)
        trains_at_time = leaving.get(departure_time, [])
        trains_at_time.append(arrival_time)
        leaving[departure_time] = trains_at_time

    departure_times = sorted(leaving.keys())
    return [(dt, leaving[dt]) for dt in departure_times]

def normalize_times(times):
    '''Normalize a departure and arrival times to minutes from midnight

    Example:
    >>> print normalize_times(('09:00','12:00'))
    [540, 720]
    '''
    def normalize(t):
        '''Normalize a times

        Example:
        >>> print normalize('16:20')
        980
        '''
        bits = [int(x) for x in t.split(':')]
        return bits[0]* 60 + bits[1]


    return [normalize(t) for t in times]

def _usage():
    print "Usage: train_timetable.py <input_file> <output_file>"
    print "If output_file omitted, printed to stdout"

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        _usage()
        print "Running test suite..."
        failed, total = _test()
        if (not failed): print "All %d tests passed"%total
    elif len(sys.argv) == 2:
        inputs = file(sys.argv[1]).read()
        print train_timetable(inputs)
    elif len(sys.argv) == 3:
        inputs = file(sys.argv[1]).read()
        file(sys.argv[2],"w").write(train_timetable(inputs))
    else:
        _usage()
        sys.exit(1)
