#!/usr/bin/env python
""" 
    saving_the_universe.py
    solution to Saving the Universe problem
    
    Copyright (C) 2008 Masood Behabadi <masoodbeh@gmail.com>
"""
from sys import stdin

cases = []  # list of cases

# parsing input data
totalCases = int(stdin.readline())   # total number of cases
for case in xrange(totalCases):
    engines = []
    for i in xrange(int(stdin.readline())):
        engines.append(stdin.readline().rstrip())
    
    queries = []
    for i in xrange(int(stdin.readline())):
        queries.append(stdin.readline().rstrip())
    
    cases.append((engines, queries))
    
caseN = 1
for case in cases:
    engines, queries = case
    switchCount = 0
    
    engineList = list(engines)
    for query in queries:
        if query in engineList:
            engineList.remove(query)
                    
        # if engineList became empty search engine must be switched
        if (len(engineList) == 0):
            switchCount = switchCount + 1
            engineList = list(engines)
            engineList.remove(query)
        
    print "Case #%s: %s" % (caseN, switchCount)
    
    caseN = caseN + 1

