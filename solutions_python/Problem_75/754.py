#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

combine_set = {}
oppose_set = []

def combine(elem):
	global combine_set
	if len(elem) < 2:
		return False
	elif (elem[-1], elem[-2]) in combine_set.keys():
		c1 = elem.pop()
		c2 = elem.pop()
		elem.append( combine_set[(c1, c2)] )
		return True
	elif (elem[-2], elem[-1]) in combine_set.keys():
		c1 = elem.pop()
		c2 = elem.pop()
		elem.append( combine_set[(c2, c1)] )
		return True
	else:
		return False
	return False

def oppose(elem):
	global oppose_set
	if len(elem) < 2:
		return
	for i in range(len(elem)):
		for j in range(i, len(elem)):
			if (elem[i], elem[j]) in oppose_set or (elem[j], elem[i]) in oppose_set:
				return True

def solve_b(infile):
	f = open(infile)
	ntest = int(f.readline())
	global combine_set
	global oppose_set
	
	for i in range(ntest):
		dat = f.readline().rstrip().split()
		combine_set = {}
		oppose_set = []
		
		# read combine
		c = int(dat.pop(0))
		for j in range(c):
			s = dat.pop(0)
			combine_set[(s[0], s[1])] = s[2]

		# read oppose
		d = int(dat.pop(0))
		for j in range(d):
			s = dat.pop(0)
			oppose_set.append((s[0], s[1]))

		n = int(dat.pop(0))
		invokes = list(dat.pop(0))
		elem = []

		for j in range(n):
			elem.append(invokes.pop(0))
			while combine(elem):
				pass
			if oppose(elem):
				elem = []
		
		print "Case #%d: [%s]" % ( i+1, ', '.join(elem) )

def main():
	if len(sys.argv) > 1:
		solve_b(sys.argv[1])
	else:
		print "no input file."

if __name__ == '__main__':
	main()

