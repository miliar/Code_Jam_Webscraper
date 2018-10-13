#!/usr/bin/env python

# Author: Uldis Bojars
#         captsolo.net

# PRINT_CASES = True
PRINT_CASES = False

import os


def read_paths(inp, out):
    paths = {}

    for item in inp:
        tmp = item
        while tmp != "/":
            paths[tmp] = True
            head, tail = os.path.split(tmp)
            tmp = head

    sum = 0
    for item in out:
        tmp = item
        i = 0
        while (tmp not in paths) and (tmp != "/"):
                if tmp not in paths:
                    paths[tmp] = True
                head, tail = os.path.split(tmp)
                tmp = head
                i += 1
        sum += i
    return sum
        
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
            n, m = map(int, tmp[pos].split())
            pos += 1
            src = []
            for i in xrange(0, n):
                src.append(tmp[pos].strip())
                pos += 1
            out = []
            for i in xrange(0, m):
                out.append(tmp[pos].strip())
                pos += 1
            yield (src, out)

def run_test(test_file):
    tests = TestCases(test_file)
    for i, (src, out) in enumerate(tests.cases()):
        res = read_paths(src, out)
        print "Case #%i: %s" % (i+1, res)


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
