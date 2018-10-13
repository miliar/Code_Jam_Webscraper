#!/usr/bin/env python

from sys import stdin
import math

for case in range (int(stdin.readline())):
    (a, b) = map(int, stdin.readline().split())
    ndigits = int(math.log10(a))+1
    answer = 0
    for n in xrange(a, b+1):
        consideredCandidates = set()
        for shift in xrange(1, ndigits):
            factor = 10 ** shift
            candidate = (n / factor) + (n % factor) * (10 ** (ndigits - shift))
            if (candidate in consideredCandidates):
                continue
            if (candidate > n and candidate <= b):
                answer += 1
            consideredCandidates.add(candidate)
        exit
    print "Case #%d: %s" % (case + 1, answer)
