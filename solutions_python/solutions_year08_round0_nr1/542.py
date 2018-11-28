#!/usr/bin/env python

import sys

def main ():
    cases = sys.stdin.readline().strip()
    cases = int(cases)
    print >> sys.stderr, "expecting %i cases" % cases
    for case in xrange(cases):
        solve_case(case)

def solve_case (case_num):
    switches = 0
    num_engines = count_engines()
    num_queries = sys.stdin.readline().strip()
    num_queries = int(num_queries)
    
    queries = set()
    for query in xrange(num_queries):
        query = sys.stdin.readline().strip()
        queries.add(query)
        if len(queries) >= num_engines:
            switches += 1
            queries.clear()
            queries.add(query)
    print "Case #%i: %i" % (case_num+1, switches)

def count_engines():
    engines = sys.stdin.readline().strip()
    engines = int(engines)
    print >> sys.stderr, "expecting %i engines" % engines
    for engine in xrange(engines):
        engine = sys.stdin.readline().strip()
        print >> sys.stderr, engine
    return engines

if __name__ == "__main__":
    main()
