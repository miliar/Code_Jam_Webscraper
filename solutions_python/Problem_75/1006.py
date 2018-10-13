#!/usr/bin/env python

import sys

#debug=True
debug=False
#adebug=True
adebug=False

def combines(a, b, combs):
    for c in combs:
        if a+b == c[:2] or b+a == c[:2]:
            return c[2]
    return False

def opposes(a, b, ops):
    for c in ops:
        if debug: print "C",c
        if debug: print "inp",a+b, b+a
        if a+b == c or b+a == c:
            return True
    return False

def hasopposing(new, s, ops):
    for l in s:
        if opposes(new, l, ops):
            return True
    return False

def solve (combs, ops, s):
    if debug: print "Combinations",combs
    if debug: print "Oppositions", ops
    totall = []
    for l in s:
        totals = "".join(totall)
        if len(totall) > 0:
            combstatus = combines (l, totall[-1], combs)
        else:
            combstatus = False
        if combstatus:
            totall.pop()
            totall.append(combstatus)
        elif hasopposing(l, totals, ops):
            totall = []
        else:
            totall.append(l)
        if adebug: print totall
    return "[" + ", ".join(totall) + "]"



inputf = sys.stdin
inp = inputf.readlines()

totalinp = int(inp[0].strip())

if debug:
    print inp
    print totalinp
    print 

for i in xrange(1,totalinp+1):
    combinations = []
    oppositions = []
    cinps = inp[i].strip()
    cinpl = cinps.split(" ")
    if debug: print cinpl

    ccombcount = int(cinpl.pop(0))
    if debug: print "comb count",ccombcount
    for k in xrange(ccombcount):
        combinations.append(cinpl.pop(0))

    coppcount = int(cinpl.pop(0))
    if debug: print "opposition count",coppcount
    for l in xrange(coppcount):
        oppositions.append(cinpl.pop(0))

    testlen = int(cinpl.pop(0))
    if debug: print "testlen", testlen

    teststr = cinpl[0]
    if debug: print "teststr", teststr


    print "Case #%d: %s" % (i , solve (combinations, oppositions, teststr))
        



