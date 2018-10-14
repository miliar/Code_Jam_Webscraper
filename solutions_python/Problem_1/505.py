#!/usr/bin/python

import sys
from copy import copy

sys.setrecursionlimit(1500)

def get_set():
	num = int(sys.stdin.readline()[:-1])
	return [sys.stdin.readline()[:-1] for i in range(0, num)]

def test_set(engines, searches, cur_engine=False, switches=0):
	#print cur_engine
	try:
		search = searches[0]
	except IndexError:
		return switches
	#print "%s == %s" % (cur_engine, search)
	if cur_engine == search or not cur_engine:
		possible_engines = engines
		for next_search in searches:
			possible_engines = [possible_engine for possible_engine in possible_engines if possible_engine != next_search]
			if len(possible_engines) == 1:
				break
		engine = possible_engines[0]
		new_switches = switches
		if cur_engine != False:
			new_switches += 1
		return test_set(engines, searches[1:], cur_engine=engine, switches=new_switches)
	return test_set(engines, searches[1:], cur_engine=cur_engine, switches=switches)

cases = int(sys.stdin.readline()[:-1])

for i in range(1, cases + 1):
	engines = get_set()
	searches = get_set()

	#print "Case #", i
	#print len(engines), " Engines:", engines
	#print len(searches), "Searches:", searches
	#print "Switches:", test_set(engines, searches)
	print "Case #%d: %d" % (i, test_set(engines, searches))
