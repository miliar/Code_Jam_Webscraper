#!/usr/bin/env python

import sys, os, re


def solve(f):
	lst = f.readline().split()
	l = 0
	
	c = int(lst[l]); l+=1
	lc = lst[l:l+c]; l+=c
	
	d = int(lst[l]); l+=1
	ld = lst[l:l+d]; l+=d

	s = lst[-1]
	# print lc, ld, s
	r = ''
	for x in s:
		r += x
		chg = True
		while chg:
			chg = False
			for rule in lc:
				#print r, ' ', rule
				if r[-2:] == rule[:2] or r[-2:] == rule[1]+rule[0]:
					r = r[:-2] + rule[2]
					chg = True
		for rule in ld:
			if rule[0] in r and r[-1] == rule[1]:
				r = ''
				break
			if rule[1] in r and r[-1] == rule[0]:
				r = ''
				break
	return '[' + ', '.join(r) + ']'
	
	return 0

def main():
	tt = int(sys.stdin.readline())
	for t in xrange(tt):
		res = solve(sys.stdin)
		print "Case #%d:" % (t+1), res


if __name__ == "__main__":
	main()
