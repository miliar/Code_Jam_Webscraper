from __future__ import with_statement
import sys
import re
from decimal import Decimal

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())
    weightRE = re.compile(r'\([\s]*([.0-9]+)')
    featureRE = re.compile('([a-z]+)')
    endRE = re.compile(r'\)')

    for c in xrange(1, num_cases+1):
        num_lines = int(f.readline())
        tree = [f.readline() for l in xrange(num_lines)]
        num_animals = int(f.readline())
        animals = [f.readline().split() for l in xrange(num_animals)]

        print "Case #%d:" % c
        for a in animals:
            match, depth, d, p = True, 1, 0, Decimal(1)
            for line in tree:
                w = weightRE.search(line)
                e = endRE.search(line)
                if w is not None:
                    d += 1
                if match is False:
                    if depth == d:
                        match = True
                    d -= 1 if e is not None else 0
                    continue
                if depth == d and w is not None:
                    #print line, p
                    p *= Decimal(w.group(1))
                    F = featureRE.search(line)
                    if F is None:
                        break
                    depth += 1
                    match = True if F.group(1) in a else False
                d -= 1 if e is not None else 0
            print "%.6f" % p

