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
            yield tmp[pos]
            pos += 1


def run_test(test_file):
    tests = TestCases(test_file)
    for num, case in enumerate(tests.cases()):
        n, k = [int(x) for x in case.split()]
        tmpl = (1 << n) - 1
        res = k & tmpl == tmpl

        out = "ON" if res else "OFF"
        print "Case #%i: %s" % (num+1, out)


def mock_test():
    test = """\
4
1 0
1 1
4 0
4 47
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
