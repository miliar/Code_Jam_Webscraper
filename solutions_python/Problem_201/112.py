import sys
import random
import re
import itertools
import math
import copy
import bisect
import Queue
from collections import Counter
from multiprocessing import Pool

verbose = False


def read():
    # *only* read data for a single test case
    n, k = [int(u) for u in sys.stdin.readline().split()]
    
    return n, k


def write(res):
    # write answer for a single test case
    print res[0], res[1]


def solve(data):
    n, k = data
    
    k_base2 = str(bin(k))[2:]
    m_base2 = str(bin(n+1))[2:]
    
    u = len(k_base2)
    a = (n+1)/2**u - 1
    x = (n+1) % 2**u
    
    res = [a, a]
    # print u, a, x, k - 2**(u-1)
    
    assert 0 <= k - 2**(u-1) < 2**(u-1)
    
    if k - 2**(u-1) < x:
        res[0] += 1
    if k < x:
        res[1] += 1
    
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return res


def check(data):
    
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    
    return res


if __name__ == '__main__':
    check_mode = False
    parallelize = False
    
    if len(sys.argv) > 1 and "-v" in sys.argv[1:]:
        verbose = True
    
    if len(sys.argv) > 1 and "-c" in sys.argv[1:]:
        check_mode = True
    
    if len(sys.argv) > 1 and "-p" in sys.argv[1:]:
        parallelize = True
        i = sys.argv.index("-p")
        if len(sys.argv) > i+1 and sys.argv[i+1].isdigit():
            processes = int(sys.argv[i+1])
        else:
            processes = 2
        
    t = int(sys.stdin.readline())
    if verbose:
        print >> sys.stderr, "Solving %d test cases" % t
    
    # read input
    test_cases = [read() for i in xrange(t)]
    
    # solve
    if parallelize:
        process_pool = Pool(processes=processes)
        if check_mode:
            test_results = process_pool.map_async(check, test_cases).get(9999999)
        else:
            test_results = process_pool.map_async(solve, test_cases).get(9999999)
    
    else:
        if check_mode:
            test_results = [check(data) for data in test_cases]
        else:
            test_results = [solve(data) for data in test_cases]
    
    if verbose:
        sys.stderr.write("\n")
        sys.stderr.flush()
    
    # write output
    for i, res in enumerate(test_results):
        print "Case #%d:" % (i+1),
        write(res)


