#!/usr/bin/env python

debug = False

def read_data():
    n = int(raw_input())
    cases = []
    for i in range(n):
        case = {}

        s = int(raw_input())
        case["engines"] = []
        for j in range(s):
            case["engines"].append(raw_input())
        q = int(raw_input())
        case["queries"] = []
        for j in range(q):
            case["queries"].append(raw_input())

        cases.append(case)

    return cases

def process(engines, queries):
    switches = 0
    free_engines = engines[:]

    for query in queries:
        if query in free_engines:
            if len(free_engines) == 1:
                if debug:
                    print "!SWITCH!"
                switches += 1
                free_engines = engines[:]
            free_engines.remove(query)
        if debug:
            print query

    return switches

for i, case in enumerate(read_data()):
    print "Case #%d: %d" % (i+1, process(**case))
