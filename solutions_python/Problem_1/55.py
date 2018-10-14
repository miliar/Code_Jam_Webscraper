#!/usr/bin/python

import os
import sys

DEBUG = 0 or os.getenv("DEBUG")

def debug(*what):
    if DEBUG:
        sys.stderr.write("[DEBUG] " + " ".join(map(str, what)) + "\n")

#------------------------------------------------------

def solve_case():
    s = input()
    se = dict()
    for i in xrange(s):
        se[raw_input()] = i + 1
    q = input()
    sw = 0
    ss = set()
    for i in xrange(q):
        query = raw_input()
        debug('query', query)
        w = se[query] if se[query] else 0
        debug('w', w)
        if w and w not in ss:
            ss.add(w)
            if len(ss) == s:
                sw += 1
                ss = set([w])
                debug('sw', sw)
        debug('ss', ss)
    return sw

def main():
    for case in xrange(input()):
        print "Case #%d: %d" % (case + 1, solve_case())

main()
