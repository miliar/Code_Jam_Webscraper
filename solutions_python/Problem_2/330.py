#!/usr/bin/env python

"""
    N: cases
    T: turnaround
    NA: trips from A to B
    NB: trips from B to A
"""
__author__ = "Yoan Blanc <yoan@dosimple.ch>"

import os
import re
import sys

MODE = "debug"

MODES = {
    "small": {
        "in": "B-small.in",
        "out": "B-small.out",
    },
    "large": {
        "in": "B-large.in",
        "out": "B-large.out",
    },
    "debug": {
        "in": "B.in",
        "test": "B.test"
    }
}

def parse_input(filename):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "r")
    
    cases = []
    try:
        N = int(fp.next())
        for case in xrange(N):
            T = int(fp.next())
            NA, NB = [int(n) for n in fp.next()[:-1].split(" ")]
            departures = []
            arrivals = []
            for trip in xrange(NA + NB):
                t = [time_to_minutes(t) for t in fp.next()[:-1].split(" ")]
                t[1] += T # add the turnaround to arrival
                departures.append(t)
                arrivals.append([t[1], t[0]])
            
            case = {
                "a_to_b": {
                    "size": NA,
                    "departures": departures[:NA],
                    "arrivals": arrivals[:NA]
                },
                "b_to_a": {
                    "size": NB,
                    "departures": departures[NA:],
                    "arrivals": arrivals[NA:]
                }
            }

            for way in ("a_to_b", "b_to_a"):
                for dir in ("departures", "arrivals"):
                    case[way][dir].sort()
                    case[way][dir].reverse()

            cases.append(case)
    finally:
        fp.close()
    
    return cases

def generate_output(filename, results):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "w")

    i = 0
    for result in results:
        i+=1
        fp.write("Case #%d: %s\n" % (i, result))
    fp.close()

def calc_results(cases):
    results = []
    i = 0
    for case in cases:
        i += 1
        counters = {
            "a_to_b": 0,
            "b_to_a": 0
        }
        while case["a_to_b"]["size"] or case["b_to_a"]["size"]:
            if case["a_to_b"]["size"] and case["b_to_a"]["size"]:
                if case["a_to_b"]["arrivals"][-1][0] < case["b_to_a"]["arrivals"][-1][0]:
                    way = "a_to_b"
                else:
                    way = "b_to_a"
            elif case["a_to_b"]["size"]:
                way = "a_to_b"
            else:
                way = "b_to_a"
            
            arr = case[way]["arrivals"].pop()
            trip = [arr[1], arr[0]]
            case[way]["departures"].remove(trip)
            case[way]["size"] -= 1
            counters[way] += 1

            way = "a_to_b" if way == "b_to_a" else "b_to_a"
            find_trips(case, way, trip)
        results.append("%(a_to_b)d %(b_to_a)s" % counters)
    return results

def find_trips(case, way, trip):
    """
    Finding matches from the end
    """
    for t in xrange(1, case[way]["size"]+1):
        if case[way]["departures"][-t][0] >= trip[1]:
            trip = case[way]["departures"][-t]
            case[way]["departures"].remove(trip)
            dep = [trip[1], trip[0]]
            case[way]["arrivals"].remove(dep)
            case[way]["size"] -= 1
            
            way = "a_to_b" if way == "b_to_a" else "b_to_a"
            return find_trips(case, way, trip)

def test(filename, results):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "r")
    
    case = re.compile(r'Case\s#(?P<index>\d+):\s+(?P<result>.+)')
    try:
        for line in fp:
            matches = case.match(line)
            if matches:
                index = int(matches.group("index"))
                assert results[index-1] == matches.group("result"), "Case %d:\n expected:\t%s\n got:\t\t%s" % (index, matches.group("result"), results[index-1])
            else:
                raise Exception, "line fail: %s" % line
    finally:
        fp.close()

def time_to_minutes(time):
    """
    transform a time string into a float

    >>> time_to_minutes("12:00")
    720
    >>> time_to_minutes("12:30")
    750
    """
    H, M = [int(t) for t in time.split(":")]
    return H*60 + M

def main(argv):
    if len(argv) > 1 and argv[1] in MODES:
        mode = MODES[argv[1]]
    else:
        mode = MODES[MODE]

    cases = parse_input(mode["in"])
    results = calc_results(cases)
    
    if "test" in mode:
        try:
            test(mode["test"], results)
            print "all %s tests are ok" % len(results)
        except AssertionError, e:
            print e
    else:
        generate_output(mode["out"], results)
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
