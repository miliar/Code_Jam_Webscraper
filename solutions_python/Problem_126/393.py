#!/usr/bin/env python
""" Code Jam 2013 - Round 1C - Problem A """
import sys
import re


def generate_substring(s):
    for start in range(0, len(s) + 1):
        for end in range(0, len(s) + 1):
            yield s[start:end]


def n_value(name, n):
    consonants = re.compile(r'([b-df-hj-np-tv-z]){%d}' % n)

    count = 0

    for s in generate_substring(name):
        if consonants.search(s):
            count += 1

    return count

if __name__ == '__main__':
    # Read args
    if len(sys.argv) != 3:
        print "USAGE: a.py in_file.in out_file.out"
        sys.exit(1)

    with open(sys.argv[1], 'rU') as fin, open(sys.argv[2], 'w') as fout:
        T = int(fin.readline())

        for case in xrange(1, T+1):
            name, n = fin.readline().split()
            soln = n_value(name, int(n))

            print >> fout, "Case #{0}: {1}".format(case, soln)
