#!/usr/bin/env python
"""
Train Timetable
"""
from datetime import time, timedelta
import sys

#
# Helpers
#
class Time(time):
    """A time class that supports basic arithmetic operations with timedelta.

    >>> time_from_str('10:25') + timedelta(minutes=5)
    10:30
    >>> Time(5, 30) + timedelta(minutes=30)
    06:00
    >>> Time(5, 29) + timedelta(minutes=30)
    05:59
    >>> Time(6, 0) + timedelta(minutes=120)
    08:00
    >>> Time(6, 0) + timedelta(minutes=90) == Time(7,30)
    True
    >>> Time(2, 30) < Time(14, 30)
    True
    """
    def __add__(self, other):
        minutes = other.seconds / 60 + self.minute
        hours = (minutes / 60 if minutes >= 60 else 0)
        minutes = minutes - hours * 60
        try:
            return Time(self.hour + hours, minutes)
        except ValueError:
            # HACK: Don't overflow to the next day.
            return Time(23, 59)

    def __repr__(self):
        return '%02d:%02d' % (self.hour, self.minute)

def time_from_str(time_str):
    hour, minute = time_str.split(':')
    return Time(int(hour), int(minute))


#
# Handle case
#
def do_case(trips_AB, trips_BA, turnaround_time):
    start_times_A = [time_from_str(a.split()[0]) for a in trips_AB]
    start_times_B = [time_from_str(b.split()[0]) for b in trips_BA]
    start_times_A.sort()
    start_times_B.sort()
    next_departures_B = [time_from_str(a.split()[1]) + timedelta(minutes=turnaround_time) for a in trips_AB]
    next_departures_A = [time_from_str(b.split()[1]) + timedelta(minutes=turnaround_time) for b in trips_BA]
    num_start_A = num_start_B = 0
    
    for a in start_times_A:
        candidates_A = [next_a for next_a in next_departures_A if a >= next_a]
        if not any(candidates_A):
            num_start_A += 1
        # Get rid of used candidate.
        if candidates_A:
            next_departures_A.pop(next_departures_A.index(min(candidates_A)))
            
    for b in start_times_B:
        candidates_B = [next_b for next_b in next_departures_B if b >= next_b]
        if not any(candidates_B):
            num_start_B += 1
        # Get rid of used candidate.
        if candidates_B:
            next_departures_B.pop(next_departures_B.index(min(candidates_B)))

    return (num_start_A, num_start_B)

#
# Main
#
def main(lines):
    """
    >>> main(open('sample.txt', 'r').read().splitlines())
    Case #1: 2 2
    Case #2: 2 0
    Case #3: 3 2
    """

    num_cases = int(lines[0])
    lines = lines[1:]

    for case in xrange(1, num_cases + 1):
        start_offset = 0
        trips_AB = []
        trips_BA = []

        # Get turnaround time
        turnaround_time = int(lines.pop(0))

        num_trips_AB, num_trips_BA = lines.pop(0).split()

        # Get A->B time schedule.
        for n in xrange(int(num_trips_AB)):
            trips_AB.append(lines.pop(0))

        # Get B->A time schedule.
        for n in xrange(int(num_trips_BA)):
            trips_BA.append(lines.pop(0))

        # Calculate case and display results.
        num_start_A, num_start_B = do_case(trips_AB, trips_BA, turnaround_time)
        print 'Case #%d: %d %d' % (case, num_start_A, num_start_B)

        lines = lines[start_offset:]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s <input>' % (sys.argv[0])
        raise SystemExit

    if sys.argv[1] == 'test':
        import doctest
        doctest.testmod()
        raise SystemExit

    try:
        main(open(sys.argv[1], 'r').read().splitlines())
    except IOError, e:
        print 'Fatal error:', e
