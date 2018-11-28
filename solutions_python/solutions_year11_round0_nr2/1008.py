#!/usr/bin/env python

import sys

try:
    filename = sys.argv[1]
except Exception as e:
    print str(e)
    exit()

file = open(filename)
test_cases = int(file.readline())

def invoke(combodict, opposeddict, invocation):
    elems = []
    for c in invocation:
	elems.extend(c)
	if len(elems) > 1:
	    combo = elems[-2] + elems[-1]
	    if combo in combodict:
		elems = elems[0:-2]
	        elems.extend(combodict[combo])
	    else:
		for char1 in elems[:-1]:
		    opp = char1 + elems[-1]
		    if opp in opposeddict:
			elems = []
			break
    string = '['
    for i in xrange(len(elems)):
	string += elems[i]
	if i < len(elems) - 1:
	    string += ', '
    string += ']'
    return string

i = 0
for case in file:
    fields = case.strip().split(' ')
    #print fields
    C = int(fields[0])
    fields = fields[1:]
    combos = fields[0:C]
    combodict = {}
    for combo in combos:
	combodict[combo[0] + combo[1]] = combo[2]
	combodict[combo[1] + combo[0]] = combo[2]
    fields = fields[C:]
    D = int(fields[0])
    fields = fields[1:]
    opposed = fields[0:D]
    opposeddict = {}
    for opp in opposed:
	opposeddict[opp[0] + opp[1]] = True
	opposeddict[opp[1] + opp[0]] = True
    fields = fields[D:]
    N = int(fields[0])
    fields = fields[1:]
    invocation = fields[0]
    fields = fields[1:]
    i += 1
    
    #print combodict, opposeddict, invocation
    print 'Case #' + str(i) + ":", invoke(combodict, opposeddict, invocation)
