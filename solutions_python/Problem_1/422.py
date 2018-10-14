#!/usr/bin/env python

from sys import argv

def count_switches(engine_names, queries):
    i = 0
    j = 0
    allowed_engines = list(engine_names)
    switches = 0
    while i <= len(queries):
        sublist = list(queries[j:i])
        for engine in allowed_engines:
            if engine in sublist:
                allowed_engines.remove(engine)
        if len(allowed_engines) == 0:
            switches += 1
            i -= 1
            j = i
            allowed_engines = list(engine_names)
        i += 1
    return switches

try:
    f = open(argv[1], "rb")
except:
    f = open("data.txt", "rb")
num_cases = int(f.readline())
for case in xrange(num_cases):
    num_engines = int(f.readline())
    engine_names = []
    queries = []
    for i in xrange(num_engines):
        name = f.readline()
        engine_names.append(name)
    num_queries = int(f.readline())
    for i in xrange(num_queries):
        query = f.readline()
        queries.append(query)
    print "Case #%d: %d" % (case + 1, count_switches(engine_names, queries))
