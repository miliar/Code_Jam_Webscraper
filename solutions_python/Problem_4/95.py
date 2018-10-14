#!/usr/bin/python

import os
import sys

#sys.stdin = open('A-small-attempt0.in', 'r')
#sys.stdout = open('A-small-attempt0.out', 'w')

#sys.stdin = open('A-small-attempt1.in', 'r')
#sys.stdout = open('A-small-attempt1.out', 'w')

#sys.stdin = open('A-small.in', 'r')
#sys.stdout = open('A-small.out', 'w')

#sys.stdin = open('A-large.in', 'r')
#sys.stdout = open('A-large.out', 'w')

#sys.stderr = open('log', 'r')

DEBUG = 0 or os.getenv("DEBUG") == '1'

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#-----------------------------------------------------------------------------

for case in xrange(input()):
    debug()
    debug("Case #%d:" % (case + 1))

    n = input()
    v1 = sorted(map(int, raw_input().split()))
    v2 = sorted(map(int, raw_input().split()), reverse = True)
    sp = sum([x * y for x, y in zip(v1, v2)])

    print "Case #%d: %s" % (case + 1, sp)
