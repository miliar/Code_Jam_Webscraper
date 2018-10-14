#!/usr/bin/python

import sys

def find_optimal_switch_count(search_engines, queries):
    check_engines=[0]*len(search_engines)
    switch_count = 0
    for query in queries:
        check_engines[search_engines.index(query)] += 1
        if not 0 in check_engines:
            switch_count += 1
            check_engines=[0]*len(search_engines)
            check_engines[search_engines.index(query)] += 1
    return switch_count

def main():
    num_cases = int(sys.stdin.readline())
    for i in xrange(num_cases):
        num_search_engines = int(sys.stdin.readline())
        search_engines = [None] * num_search_engines
        for j in xrange(num_search_engines):
            search_engines[j] = str(sys.stdin.readline())
        num_queries = int(sys.stdin.readline())
        queries = [None] * num_queries
        for j in xrange(num_queries):
            queries[j] = str(sys.stdin.readline())
        print "Case #%s: %s" % (i+1, 
                            find_optimal_switch_count(search_engines, queries))
    return 0

if __name__ == "__main__":
    exit_status = main()
    sys.exit(exit_status)
