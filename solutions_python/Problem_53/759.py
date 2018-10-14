#!/usr/bin/python

import sys
import re

snaps_to_get_on = {0:0}

def num_snaps_on(num_snappers):
    if num_snappers in snaps_to_get_on:
        return snaps_to_get_on[num_snappers]
    max_calculated_so_far = max(snaps_to_get_on.keys())
    for i in xrange(max_calculated_so_far+1, num_snappers+1):
        snaps_to_get_on[i] = snaps_to_get_on[i-1]*2 + 1
    return snaps_to_get_on[num_snappers]

def test_case(num_snappers, num_snaps):
    on_snaps = num_snaps_on(num_snappers)
    if (num_snaps + 1) % (on_snaps + 1) == 0:
        return True
    return False

if __name__=='__main__':
    testfile = open(sys.argv[1], 'r')
    num_tests = int(testfile.next())
    for i in xrange(1, num_tests+1):
        [num_snappers, num_snaps] = [int(x) for x in re.split(r'\D+', testfile.next().strip())]
        result = test_case(num_snappers, num_snaps)
        print "Case #%d: %s" % (i, result and 'ON' or 'OFF')
    testfile.close()
