#!/usr/bin/env python2.5
# -*- coding: iso-8859-1 -*-

#
# Google CodeJam Entry
#
# Usage <scriptname>.py inputfile >outputfile
#
# Copyright 2008 AussieSteve
#

from __future__ import with_statement

from optparse import OptionParser
import sys
import re
import math


parser = OptionParser()
parser.add_option("-d", "--debug", action="store_true", dest="debug")

(options, args) = parser.parse_args()

def decorator(old_decorator):
    "Restore original name, doc & dict for decorated functions"
    def new_decorator(f):
        g = old_decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g

    new_decorator.__name__ = old_decorator.__name__
    new_decorator.__doc__ = old_decorator.__doc__
    new_decorator.__dict__.update(old_decorator.__dict__)

    return new_decorator

def memoize(cache=None):
    """Decorator to memoize a function
    Can be used on multiple functions
    Warning: Does not reclaim memory"""

    if cache == None:
        cache = {}

    @decorator
    def m(f):
        def g(*args, **kwargs):
            key = ( f, tuple(args), frozenset(kwargs.items()) )
            if key not in cache:
                cache[key] = f(*args, **kwargs)
            return cache[key]

        return g

    return m

def combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in combinations(items[i+1:],n-1):
                yield [items[i]]+cc

# Input file is first argument if present, or stdin
if args:
    input_filename = args[0]

    file = open(input_filename, 'r')
else:
    file = sys.stdin

num_tests = int(file.readline())
if options.debug:
    print "num_tests", num_tests

for test in range(1, num_tests + 1):
    likes = {}
    satisfies = {}
    flavors = int(file.readline())
    for flavor in range(1, flavors + 1):
        satisfies[flavor] = {0: [], 1: []}
    customers = int(file.readline())
    for customer in range(customers):
        cust = map(int, file.readline().split())
        t = cust.pop(0)
        for i in range(t):
            flavor = cust.pop(0)
            malted = cust.pop(0)
            satisfies[flavor][malted].append(customer)

    if options.debug:
        print 'satisfies', repr(satisfies)

    success = False
    for num_malted in range(0, flavors + 1):
        if success:
            break
        for comb in combinations(range(1, flavors + 1), num_malted):
            f = [(flav in comb) for flav in range(1, flavors + 1)]
            if options.debug:
                print "Trying", f

            satisfied = {}
            for flavor in range(len(f)):
                if f[flavor]:
                    malted = 1
                else:
                    malted = 0
                for c in satisfies[flavor + 1][malted]:
                    satisfied[c] = True
            s = satisfied.keys()
            s.sort()
            if options.debug:
                print "Satisfied", s
            if len(s) == customers:
                success = True
                break

    if success:
        print "Case #%s:" % (test,),
        r = []
        for i in range(flavors):
            if f[i]:
                r.append('1')
            else:
                r.append('0')
        print ' '.join(r)
    else:
        print "Case #%s: IMPOSSIBLE" % (test,)

