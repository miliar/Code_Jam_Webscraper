#!/usr/bin/env python

# Author: Uldis Bojars
#         captsolo.net

# PRINT_CASES = True
PRINT_CASES = False

import sys
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
            yield (tmp[pos], tmp[pos+1])
            pos += 2

def run_solver(inp):
    r, k, n = map(int, inp[0].split())
    arr = inp[1].split()
    arr = map(int, arr)

    tot_sum = {}
    next = {}

    for i, num in enumerate(arr):
        arr_sum = 0
        pos = i
        while arr_sum + arr[pos] <= k:  
            arr_sum += arr[pos] 
            pos = (pos+1) % len(arr)
            if pos == i:
                break
        tot_sum[i] = arr_sum
        next[i] = pos

    tmp = 0
    pos = 0

    init_steps = -1
    init_sum = 0
    rem = r

    while rem > 0:
        if pos == 0 and tmp > 0 and init_steps == -1:
            init_sum = tmp
            init_steps = r - rem
            tmp += (rem / init_steps) * init_sum
            rem = rem % init_steps
        else:
            tmp += tot_sum[pos]
            pos = next[pos]
            rem -= 1
        
    return tmp

def run_test(test_file):
    tests = TestCases(test_file)
    for num, case in enumerate(tests.cases()):

        print "Case #%i: %s" % (num+1, run_solver(case))


def mock_test():
    test = """\
3
5 6 4
1 4 2 1
100 10 1
1
30 5 10
2 4 2 3 4 2 1 2 1 3
"""
    test2 = """\
3
100000000 6 4
1 4 2 1
100000000 10 1
1
100000000 5 10
2 4 2 3 4 2 1 2 1 3
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
    main()
