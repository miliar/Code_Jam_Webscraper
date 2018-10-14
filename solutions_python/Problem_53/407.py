#! /usr/bin/env python

from optparse import OptionParser
import re
import sys

LINE_REGEX = re.compile(r'(?P<snappers>\d+) (?P<snaps>\d+)')
count_cache = {}

#NOTE: For large datasets, we need to cache the results we have generated or
#      we'd get into calculation hell
def GetMinSnapCount(num_of_snappers):
    total = 0
    i = 0

    for key, value in count_cache.items():
	if abs(i - num_of_snappers) > abs(key - num_of_snappers):
	    i = key
	    total = value

    if i < num_of_snappers:
	while i < num_of_snappers:
	    total = total * 2 + 1
	    i += 1
    elif i > num_of_snappers:
	while i > num_of_snappers:
	    total = (total - 1) / 2
	    i -= 1

    return total

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
	    matches = LINE_REGEX.search(file_handle.readline())
	    snappers = int(matches.group('snappers'))
	    snaps = int(matches.group('snaps'))

	    min_snaps = GetMinSnapCount(snappers)
	    count_cache[snappers] = min_snaps
	    if (snaps == 0):
		light_on = 'OFF'
	    elif ((snaps == min_snaps) or ((snaps % (min_snaps + 1)) == min_snaps)):
		light_on = 'ON'
	    else:
		light_on = 'OFF'

	    print('Case #{0:d}: {1}'.format(case+1,light_on))
