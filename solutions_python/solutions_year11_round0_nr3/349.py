#!/usr/bin/python
import sys

def check_equal(case):
    result = 0
    for n in case:
        result ^= n
    return result == 0

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().rstrip('\n'))
    for T in xrange(1, num_cases+1):
        N = int(sys.stdin.readline().rstrip('\n'))
        test_case = [int(x) for x in sys.stdin.readline().split()]
        if check_equal(test_case):
            test_case.remove(min(test_case))
            result = str(sum(test_case))
        else:
            result = "NO"
        print "Case #%d: %s" % (T, result)
