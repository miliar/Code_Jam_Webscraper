#!/usr/bin/env python
""" Code Jam 2013 - Problem A (jaddison)"""
import math


def fair_and_square(start, stop):
    count = 0
    for i in range(start, stop + 1):
        s = str(i)
        sqrt = math.sqrt(i)
        if s == s[::-1] and sqrt.is_integer():
            n = str(int(sqrt))
            if n == n[::-1]:
                count += 1
    return count


def process(in_file):
    cases = int(in_file.readline().strip())
    results = []
    for i in range(cases):
        start, stop = in_file.readline().strip().split()
        count = fair_and_square(int(start), int(stop))
        results.append("Case #%d: %d" % (i + 1, count))
    return results


if __name__ == '__main__':
    import sys

    # Read args
    if len(sys.argv) < 2:
        print "USAGE: gcjC.py in_file.in out_file.out"

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file, 'rU') as f:
        result = process(f)

    with open(out_file, 'w') as f:
        for line in result:
            f.write("%s\n" % line)
