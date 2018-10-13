#!/bin/python

import copy

def getline():
	return f.readline().strip()

def log(msg):
#	print msg
	return

def do_case(case_num):
	"""case_num 1 based."""
	num_engines = int(getline())
	engines = {}
	for i in range(num_engines):
		line = getline()
		engines[line] = 0
		log("Adding engine %s" % line)
	
	num_searches = int(getline())
	searches = []
	for i in range(num_searches):
		line = getline()
		searches.append(line)
	log("Searches: %s" % searches)
	
	switches = 0
	current_search = 0
	avail_engines = copy.copy(engines)
	for s in searches:
		log("Search: %s" % s)
		if s in avail_engines:
			del avail_engines[s]
			log("Removed %s from avail_engines" % s)
			if len(avail_engines) == 0:
				log("All engines are used up. Need to switch")
				switches += 1
				avail_engines = copy.copy(engines)
				del avail_engines[s]
	
	print "Case #%d: %d" % (case_num, switches)

def main():
	global f
	f = open('A-large.in')
	cases = int(getline())
	log("%d cases" % cases)
	for case in range(cases):
		do_case(case + 1)

main()
