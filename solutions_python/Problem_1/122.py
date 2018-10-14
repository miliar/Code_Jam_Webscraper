#!/usr/bin/env python
"""Google Code Jam qualification round. By Hraban Luyat.

See http://google.com/codejam/ for more info.

"""
import itertools as it
import sys

USAGE = """
Usage:

    ./gcj1 INPUT_FILENAME

"""

def handle_case(engines, queries):
    s = len(engines)
    # Corresponding bit in this list is set to 1 when an engine is encountered
    # in the query list. The last engine left with no hits is the best choice
    # for the next switch.
    dirty = dict(it.izip(engines, it.repeat(0, s)))
    for i, q in enumerate(queries):
        if not dirty[q]:
            dirty[q] = 1
            s -= 1
            if s == 0:
                # This was the last search engine in the list. I.e.: this is
                # the engine that should have been used up until here. From now
                # on, use a different one: switch!
                #print >> sys.stderr, "DEBUG: Should have used %s" % q
                return 1 + handle_case(engines, queries[i:])
    # There was at least one engine available that had zero queries matching
    # it. No switch was necessary.
    return 0

def handle_case_no_recur(engines, queries):
    sum = 0
    while queries:
        s = len(engines)
        # Corresponding bit in this list is set to 1 when an engine is encountered
        # in the query list. The last engine left with no hits is the best choice
        # for the next switch.
        dirty = dict(it.izip(engines, it.repeat(0, s)))
        for i, q in enumerate(queries):
            if not dirty[q]:
                dirty[q] = 1
                s -= 1
                if s == 0:
                    # This was the last search engine in the list. I.e.: this is
                    # the engine that should have been used up until here. From now
                    # on, use a different one: switch!
                    #print >> sys.stderr, "DEBUG: Should have used %s" % q
                    queries = queries[i:]
                    sum += 1
                    break
        if s == 0:
            continue
        # There was at least one engine available that had zero queries matching
        # it. No switch was necessary.
        break
    return sum

def gcj1(path):
    f = open(path, "r")
    n = int(f.readline().strip())
    for i in xrange(1, n + 1):
        num_engines = int(f.readline().strip())
        engines = []
        for j in xrange(num_engines):
            engines.append(f.readline().strip())
        num_queries = int(f.readline().strip())
        queries = []
        for j in xrange(num_queries):
            queries.append(f.readline().strip())
        print "Case #%d: %d" % (i, handle_case_no_recur(engines, queries))

def main():
    #print __doc__
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        #sys.exit(USAGE)
        print >> sys.stderr, USAGE
        sys.exit(1)
    gcj1(sys.argv[1])

if __name__ == "__main__":
    main()
