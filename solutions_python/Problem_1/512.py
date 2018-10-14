#!/usr/bin/env python

"""Script to calculate minimum number of search engine switches.
   Google Code Jam, Qualifying Round, Problem A."""

import sys

def clear_mask(se_list):
    """Returns an initialized structure indicating that no search engine's have
    been queried for themselves yet."""
    return {}

def set_mask(Mask, query):
    """Updates the Mask structure to indicate that the search engine query
    passed, would be queried if not switched."""
    if not Mask.has_key(query): Mask[query] = True
    return Mask

def all_mask_set(Mask, se_list):
    """Boolean function that evaluates to True if all search engines have been
    queried, and False otherwise."""
    for s in se_list:
        if not Mask.has_key(s): return False
    return True

def calc_switches(se_list, query_list):
    """Determine minimal number of search engine switches required given a list
    of search engines, and a list of queries."""
    num_switches = 0
    M = clear_mask(se_list)
    for q in query_list:
        M = set_mask(M, q)
        if all_mask_set(M, se_list):
            num_switches += 1
            M = clear_mask(se_list)
            M = set_mask(M, q)  #can't "switch" to the se we just switched to
    return num_switches

def useage():
    """Display instructions to the user."""
    print "useage: " + sys.argv[0] + " FILE"
    print "where FILE is the path and name of a valid input file"

def read_from(fh, num):
    """Reads num lines from the open filehandle fh.  Returns lines as a list.
    Assumes fh is open and contains at least num lines from current offset"""
    return [fh.readline() for i in xrange(num)]

def main(args):
    """Point of code entry.  Command name in args[0], any additional args
    passed are in the remainder of the args array."""
    if len(args) < 2:
        useage()
        return 1
    num_cases = -1
    try:
        f = open(args[1])
        num_cases = int(f.readline())
        assert 0 < num_cases <= 20
        for case in xrange(num_cases):
            num_se = int(f.readline())
            assert (2 <= num_se <= 100)
            se_list = read_from(f, num_se)
            num_queries = int(f.readline())
            assert 0 <= num_queries <= 1000
            query_list = read_from(f, num_queries)
            print "Case #" + str(case+1) + ": " + str(calc_switches(se_list,
                                                                query_list))
    except IOError:
        print "Invalid file input"
        useage()
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))
