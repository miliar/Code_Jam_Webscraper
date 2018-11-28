#!/usr/bin/python

import sys
data = filter(None, map(lambda x:x.strip(), open(sys.argv[1]).readlines()))

def pop_int(data):
    return int(data.pop(0))

def pop_rows(data, num_rows):
    result = data[:num_rows]
    for i in range(num_rows):
        data.pop(0)
    return result

def pop_case(data):
    num_engines = pop_int(data)
    engines = pop_rows(data, num_engines)
    num_queries = pop_int(data)
    queries = pop_rows(data, num_queries)
    return engines, queries

def greedy_search_one(engine, queries):
    try:
        streak = queries.index(engine)
    except ValueError:
        return len(queries)
    return streak

def greedy_search_all(engines, queries):
    return max(map(lambda x: greedy_search_one(x, queries), engines))

num_cases = pop_int(data)
for case_num in range(1, num_cases+1):
    engines, queries = pop_case(data)
    num_switches = 0
    while queries:
        longest_streak = greedy_search_all(engines, queries)
        queries = queries[longest_streak:]
        if queries:
            num_switches += 1
    print "Case #%d: %d" % (case_num, num_switches)
