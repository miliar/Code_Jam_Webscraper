#!/bin/python

import copy

def getline():
	return f.readline().strip()

def log(msg):
#	print msg
	return

def do_case(case_num):
	"""case_num 1 based."""
	num_elems = int(getline())
	v1 = [int(s.strip()) for s in getline().split()]
	log(v1)
	v2 = [int(s.strip()) for s in getline().split()]
	log(v2)
	v1.sort()
	v2.sort()
	v2.reverse()
	total = 0
	for i in range(num_elems):
		total += v1[i] * v2[i]
	print "Case #%d: %d" % (case_num, total)

def main():
	global f
	f = open('A-large.in')
	cases = int(getline())
	log("%d cases" % cases)
	for case in range(cases):
		do_case(case + 1)

main()
