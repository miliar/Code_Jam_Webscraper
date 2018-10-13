#!/usr/bin/env python
import sys

def usage(prog_name):
    print >>sys.stderr, "Usage: %s <input-file>" % prog_name

def coaster(r,k,g):
    """
    a roller coaster that will run r times with capacity k for the
    list of groups g, where each g_i is the size of the i-th group
    and returns the money made that day
    """
    profit = 0
    pos = 0
    for i in range(r):
        """fill the coaster"""
        old_pos = pos
        seats_full = g[pos]
        pos = (pos+1) % len(g)

        while seats_full + g[pos] <= k and pos != old_pos:
            seats_full += g[pos]
            pos = (pos+1) % len(g)
        profit += seats_full
    return profit

def get_test_cases(f):
    """ can't think of a better way to get test cases from the file ... """
    while True:
        r_k_n = f.readline()
        groups = f.readline()
        if not r_k_n or not groups:
            break
        r, k, n = map(int, r_k_n.split())
        groups = map(int, groups.split())
        assert len(groups) == n
        for group in groups:
            assert group <= k
        yield (r,k,groups)

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        input = argv[1]
    except IndexError:
        usage(argv[0])
        return 1

    """ a list of 3-tuples containing (r,k,g) """
    test_cases = []

    with open(input) as f:
        num_cases = int(f.readline())
        for test_case in get_test_cases(f):
            test_cases.append(test_case)
        assert len(test_cases) == num_cases

    """ run the tests """
    for i, test_case in enumerate(test_cases):
        r, k, g = test_case
        print "Case #%d: %d" % (i+1, coaster(r,k,g))
    return 0

if __name__ == "__main__":
    sys.exit(main())
