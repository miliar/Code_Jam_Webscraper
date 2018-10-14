import sys
from collections import defaultdict


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    j = 1
    while i <= test_case_count:
        d, n = [int(m) for m in content[j].split(' ')]
        slowest = None
        while n > 0:
            j += 1
            p, s = [int(m) for m in content[j].split(' ')]
            h_time = float(d - p) / s
            if slowest is None or slowest < h_time:
                slowest = h_time
            n -= 1
        j += 1
        print("Case #%s: %s" % (i,  d / slowest))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
