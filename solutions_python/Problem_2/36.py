# Train Timetable
#
# Usage: python train.py test.in

import re
from heapq import *

def read_case(fp):
    """Returns (tatime, ab, ba).
    """

    tatime = int(fp.readline().strip())

    na, nb = [int(x) for x in fp.readline().split()]

    ab = []
    for i in range(na):
        m = re.search(r'(\d\d):(\d\d) (\d\d):(\d\d)', fp.readline())
        assert m

        deph, depm, arrh, arrm = [int(g) for g in m.groups()]
        dep = 60 * deph + depm
        arr = 60 * arrh + arrm
        ab.append((dep, arr))

    ba = []
    for i in range(nb):
        m = re.search(r'(\d\d):(\d\d) (\d\d):(\d\d)', fp.readline())
        assert m

        deph, depm, arrh, arrm = [int(g) for g in m.groups()]
        dep = 60 * deph + depm
        arr = 60 * arrh + arrm
        ba.append((dep, arr))

    return (tatime, ab, ba)

def trains(tatime, ab, ba):
    start_a = 0
    start_b = 0
    avail_a = []
    avail_b = []

    trips = []
    trips.extend((dep, arr + tatime, 'ab') for (dep, arr) in ab)
    trips.extend((dep, arr + tatime, 'ba') for (dep, arr) in ba)
    trips.sort()

    for t in trips:
        dep, arr, dir = t
        if dir == 'ab':
            if avail_a and avail_a[0] <= dep:
                heappop(avail_a)
                heappush(avail_b, arr)
            else:
                start_a += 1
                heappush(avail_b, arr)
        else:
            assert dir == 'ba'
            if avail_b and avail_b[0] <= dep:
                heappop(avail_b)
                heappush(avail_a, arr)
            else:
                start_b += 1
                heappush(avail_a, arr)
    return (start_a, start_b)

import sys
from pprint import pprint

input = open(sys.argv[1])

n = int(input.readline().strip())
for i in range(n):
    tatime, ab, ba = read_case(input)

    sa, sb = trains(tatime, ab, ba)
    
    print "Case #%d: %d %d" % (i+1, sa, sb)
