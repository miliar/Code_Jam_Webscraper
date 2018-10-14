# coding: utf-8

import os, sys, re, string
import math,random

def solve(x, r, c):
	ri, ga = "RICHARD", "GABRIEL"
	if x == 1:
		return ga
	if (r * c) < x:
		return ri
	if x == 2:
		return ga if (r * c) % 2 == 0 else ri
	key = (r, c) if r <= c else (c, r)
	table = {
		3: {
			(1, 3): ri,
			(1, 4): ri,
			(2, 2): ri,
			(2, 3): ga,
			(2, 4): ri,
			(3, 3): ga,
			(3, 4): ga,
			(4, 4): ri
		},
		4: {
			(1, 4): ri,
			(2, 2): ri,
			(2, 3): ri,
			(2, 4): ri,
			(3, 3): ri,
			(3, 4): ga,
			(4, 4): ga
		}
	}
	return table[x][key]

def main():
	T = int(sys.stdin.readline())
	for t in xrange(1, T + 1):
		x, r, c = map(int, sys.stdin.readline().strip().split(" "))
		#print "{0} {1} {2}".format(x, r, c)
		print "Case #{0}: {1}".format(t, solve(x, r, c)) 
		#print 

if __name__ == '__main__':
	main()


