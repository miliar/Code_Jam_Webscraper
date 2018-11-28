#!/usr/bin/env python2.5
# -*- coding: iso-8859-1 -*-

#
# Google CodeJam Entry
#
# Usage <scriptname>.py inputfile >outputfile
#
# Copyright 2008 AussieSteve
#
# Uses "mpmath" available from http://code.google.com/p/mpmath/
#

from __future__ import with_statement

from optparse import OptionParser
import sys
import re
import math
from mpmath import *

parser = OptionParser()
parser.add_option("-d", "--debug", action="store_true", dest="debug")

mp.dps = 100

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

for test in range(1, num_tests + 1):
    n = int(file.readline())

    result = floor((mpf(3) + sqrt(mpf(5))) ** mpf(n)) % 1000

    print "Case #%s: %03d" % (test, result)
