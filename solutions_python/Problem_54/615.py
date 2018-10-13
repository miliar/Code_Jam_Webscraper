#! /usr/bin/env python

from optparse import OptionParser
from decimal import Decimal
from fractions import gcd
import re
import sys

if __name__ == '__main__':
    # Command line parsing
    parser = OptionParser()
    (opts, args) = parser.parse_args()

    if len(args) != 1:
	print('ERROR: Supply filename')
	sys.exit(1)

    with open(args[0], 'r') as file_handle:
	cases = int(file_handle.readline())

	for case in range(cases):
	    numbers = file_handle.readline().strip().split(' ')
	    num_of_events = int(numbers[0])
	    events = [Decimal(x) for x in numbers[1:]]
	    events.sort()

	    if len(events) != num_of_events:
		print('ERROR: Number of events mismatch')
		sys.exit(1)

	    index = 1
	    intervals = []
	    while index < num_of_events:
		difference = events[index] - events[(index - 1)]
		if difference not in intervals:
		    intervals.append(difference)
		index += 1

	    next_event = Decimal(0)
	    if len(intervals) == 1:
		factor = (events[0] // intervals[0])
		if events[0] % intervals[0] != 0:
		    factor += 1
		next_event = (factor * intervals[0]) - events[0]
	    else:
		interval_gcd = gcd(intervals[0], intervals[1])
		factor = (events[0] // interval_gcd)
		if events[0] % interval_gcd != 0:
		    factor += 1
		next_event = (factor * interval_gcd) - events[0]

	    print('Case #{0:d}: {1}'.format(case+1,next_event))
