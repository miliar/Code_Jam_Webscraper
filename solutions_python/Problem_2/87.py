#!/usr/bin/env python

import re

debug = False

def read_data():
    n = int(raw_input())
    cases = []
    for i in range(n):
        case = {}
        case["t"] = int(raw_input())
        na, nb = re.search("(\d+) (\d+)", raw_input()).groups()
        na, nb = int(na), int(nb)

        case["atob"] = []
        for j in range(na):
            match = re.search("(\d+):(\d+) (\d+):(\d+)", raw_input()).groups()
            case["atob"].append((int(match[0])*60 + int(match[1]), int(match[2])*60 + int(match[3])))
        case["btoa"] = []
        for j in range(nb):
            match = re.search("(\d+):(\d+) (\d+):(\d+)", raw_input()).groups()
            case["btoa"].append((int(match[0])*60 + int(match[1]), int(match[2])*60 + int(match[3])))

        cases.append(case)

    return cases

def get_available(departure, lst):
    for item in lst:
        if item <= departure:
            if debug:
                print "Waiting train %d matched" % item
            lst.remove(item)
            return True
    return False

def process(atob, btoa, t):
    atob.sort(cmp=lambda x, y: cmp(x[0], y[0]))
    btoa.sort(cmp=lambda x, y: cmp(x[0], y[0]))
    avail_a = []
    avail_b = []
    ta = 0
    tb = 0

    while len(atob) > 0 or len(btoa) > 0:
        if len(atob) > 0 and (len(btoa) == 0 or atob[0][0] <= btoa[0][0]):
            # Train from A to B
            dep, arr = atob.pop(0)
            if debug:
                print "A %d -> %d B" % (dep, arr)
            if not get_available(dep, avail_a):
                ta += 1
            avail_b.append(arr + t)
        else:
            # Train from B to A
            dep, arr = btoa.pop(0)
            if debug:
                print "B %d -> %d A" % (dep, arr)
            if not get_available(dep, avail_b):
                tb += 1
            avail_a.append(arr + t)
    return ta, tb

for i, case in enumerate(read_data()):
    ta, tb = process(**case)
    print "Case #%d: %d %d" % (i+1, ta, tb)
