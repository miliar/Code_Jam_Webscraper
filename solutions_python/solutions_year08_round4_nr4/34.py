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
#import math
#from mpmath import *   # mpmath available from http://code.google.com/p/mpmath/
#mp.dps = 100

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

# Input file is first argument if present, or stdin
if args:
    input_filename = args[0]

    file = open(input_filename, 'r')
else:
    file = sys.stdin

num_tests = int(file.readline())
if options.debug:
    print "num_tests", num_tests

def permutations(L):
    if len(L) <= 1:
        yield L
    else:
        a = [L.pop(0)]
        for p in permutations(L):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]

def rle_length(s):
    r = 0
    last = ''
    for c in s:
        if c == last:
            pass
        else:
            last = c
            r += 1
    return r

def apply_perm(s, p):
    result = ''
    k = len(p)
    lens = len(s)
    stepping = 0
    while stepping < lens:
        for perm in p:
            result += s[stepping + perm]
        stepping += k
    return result

for test in range(1, num_tests + 1):
    k = int(file.readline())
    s = file.readline().strip()

    min_rle = rle_length(s)
    for p in permutations(range(k)):
        y = apply_perm(s, p)
        rle = rle_length(y)
        if rle < min_rle:
            min_rle = rle

    print "Case #%s: %d" % (test, min_rle)
