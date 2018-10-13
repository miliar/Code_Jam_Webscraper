#!/usr/bin/env python

# Author: Uldis Bojars
#         captsolo.net

# PRINT_CASES = True
PRINT_CASES = False

import sys
import time
from cStringIO import StringIO

class TestCases(object):
    def __init__(self, test_arr):
        self.arr = list(test_arr)

    def cases(self):
        tmp = self.arr
        num_cases = int(tmp[0])

        pos = 1

        # for all test cases
        for i in range(0, num_cases):
            yield tmp[pos]
            pos += 1

def gcd(a,b):
    # Euler's algorithm
   
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    else:
        return a

def max_gcd(inp):
    tmp_gcd = 0
    tmp_pos = 0
    pos = 0

    bound = max(inp)
    arr = list(inp)

    while pos < bound:
        #tmp = reduce(lambda x, y: gcd(x,y,pos), inp)
        for i in xrange(len(arr)):
            arr[i] = inp[i] + pos
        tmp = reduce(gcd, arr)
        if tmp > tmp_gcd:
            tmp_gcd = tmp
            tmp_pos = pos
        pos += tmp
        
    return tmp_gcd, tmp_pos


def run_solver(case):
    arr = map(int, case.split())[1:]
    return max_gcd(arr)[1]


def run_test(test_file):
    tests = TestCases(test_file)
    for num, case in enumerate(tests.cases()):

        print "Case #%i: %i" % (num+1, run_solver(case))
        sys.stdout.flush()


def mock_test():
    test = """\
3
3 26000000 11000000 6000000
3 1 10 11
2 800000000000000000001 900000000000000000001
"""

    return StringIO(test)


def main():
    import sys
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        f = open(fname)
    else:
        print "Usage: %s input_file" % (sys.argv[0],)
        print " - no parameters supplied. running example test case."
        print 
        f = mock_test()

    # f = open(fname)

    run_test(f)
    f.close()
 

if __name__ == "__main__":
    st = time.time()
    main()
    #print "Time:", int(time.time() - st)
