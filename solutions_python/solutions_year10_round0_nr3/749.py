#!/usr/bin/python

import re
import sys
from collections import deque

def test_case(runs, capacity, groups):
    groups = deque(groups)
    earnings = 0
    for r in range(runs):
        on_ride = []
        while len(groups)>0 and sum(on_ride)+groups[0]<=capacity:
            on_ride.append(groups.popleft())
        earnings = earnings + sum(on_ride)
        groups.extend(on_ride)
    return earnings

if __name__=='__main__':
    testfile = open(sys.argv[1], 'r')
    num_tests = int(testfile.next())
    for i in xrange(1, num_tests+1):
        [runs, capacity, N] = [int(x) for x in re.split(r'\D+', testfile.next().strip())]
        groups = [int(x) for x in re.split(r'\D+', testfile.next().strip())]
        result = test_case(runs, capacity, groups)
        print "Case #%d: %s" % (i, result)
    testfile.close()
