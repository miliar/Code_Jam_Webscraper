#!/usr/bin/env python
import fileinput
import sys
from collections import Counter

lines_per_case = 1


def solve_case(case):
    a, b = case[0].strip().split()
    ai, bi = int(a, 10), int(b, 10)
    l = range(1, len(a))
    counter = 0
    seen = set()

    for x in xrange(ai,bi):
        x = str(x)
        for i in l:
            c =  x[i:] + x[0:i]
            ci = int(c, 10)
            s = frozenset((x,c))
            if ai <= ci <= bi and s not in seen and c != x:
                seen.add(s)
                counter += 1

    return counter

def produce_output(index, solution):
    print 'Case #{0}: {1}'.format(index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        y = x + n_of_lines_per_case
        yield lines[x:y]
        x = y

if __name__ == "__main__":
    lines = []
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
    else:
        for line in fileinput.input():
            lines.append(line)

    if len(lines) > 0:
        #nt = int(lines[0])
        for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
            produce_output(index, str(solve_case(case)))
