#!/usr/bin/env python

import sys
import os

def run_case(handle):
    num_engines = int(handle.readline())
    engines = [handle.readline().strip() for i in range(num_engines)]

    num_queries = int(handle.readline())
    queries = [handle.readline().strip() for i in range(num_queries)]

    switches = 0
    while queries:
        engine, next_switch = best_choice(queries, engines)
        queries = queries[next_switch:]
        switches += 1

    return max(switches-1, 0)

def best_choice(queries, engines):
    """Will return the best pick for a search engine"""
    min = 1001 # MAx of 100 engines
    tries = []
    for engine in engines:
        try:
            tries.append(queries.index(engine))
        except ValueError:
            tries.append(10000)

    occurrence = max(tries)
    return tries.index(occurrence), occurrence

def main():
    handle = open(sys.argv[1])

    testcases = int(handle.readline())
    for i in range(testcases):
        print "Case #%d: %d" % (i+1, run_case(handle))

if __name__ == '__main__':
    main()
