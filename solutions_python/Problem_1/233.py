#!/usr/bin/env python
import sys

def main():
    file_in = sys.stdin
    file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        n_engines = int(file_in.readline())
        engines = []
        for j in xrange(n_engines):
            engines.append(file_in.readline()[:-1])
        queries = []
        n_queries = int(file_in.readline())
        for j in xrange(n_queries):
            queries.append(file_in.readline()[:-1])

        # processing queries
        active = set(engines)
        n_switches = 0
        for q in queries:
            if q in active:
                active.remove(q)
                if len(active) == 0:
                    n_switches += 1
                    active = set(engines)
                    active.remove(q)

        print "Case #%d: %d" % (i+1, n_switches)

    #file_out.close()
    #file_in.close()

if __name__ == '__main__':
    main()