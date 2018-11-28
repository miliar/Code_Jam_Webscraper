#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from __future__ import with_statement

from optparse import OptionParser
import sys
import re

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

def find_max(seq):
    "Return the index of the largest item in the sequence seq"
    i = 0
    m = seq[i]
    mi = i
    for i in range(len(seq)):
        if seq[i] > m:
            m = seq[i]
            mi = i
    return mi

assert find_max([3, 5, 4]) == 1
assert find_max([-3, -4, -5]) == 0
assert find_max([1, 2, 3, 4]) == 3


if args:
    input_filename = args[0]

    f = open(input_filename, 'r')

    num_tests = int(f.readline().strip())
    if options.debug:
        print "num_tests", num_tests

    for test in range(1, num_tests + 1):
        engines = {} # from name to num
        ename = {}   # from num to name
        queries = []

        num_engines = int(f.readline().strip())
        if options.debug:
            print "num_engines", num_engines
        for e in range(num_engines):
            name = f.readline().strip()
            engines[name] = e
            ename[e] = name
            if options.debug:
                print "e", e, name

        num_queries = int(f.readline().strip())
        if options.debug:
            print "num_queries", num_queries
        for q in range(num_queries):
            name = f.readline().strip()
            queries.append(engines[name])
            if options.debug:
                print 'q', q, queries[-1], name

        solution={}
        prev = {}
        for e in range(0, num_engines):
            prev[e] = 0
        for q in range(num_queries - 1, -1, -1):
            solution[q] = []
            explode = queries[q]
            for e in range(0, num_engines):
                if e == queries[q]:
                    prev[e] = 0
                else:
                    prev[e] += 1
                solution[q].append(prev[e])

        if options.debug:
            print 'solution', repr(solution)

        switches = -1
        q = 0
        while q < num_queries:
            choice = find_max(solution[q])
            if options.debug:
                print "Choosing", choice, ename[choice]
            switches += 1
            q += solution[q][choice]
        if switches < 0:
            switches = 0
        print "Case #%s: %s" % (test, switches)
