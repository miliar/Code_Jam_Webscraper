#! /usr/bin/python

from sys import stdin

def minimize_time(C, F, X):

	n = 0
	slowdown = 0
	T = X/2

	while True:

		slowdown += C/(2 + n*F)
		n += 1
		T_next = X/(2 + F*n) + slowdown

		if T_next > T:
			return T

		T = T_next

if __name__ == '__main__':
	
	N = int(stdin.readline())

	for i in xrange(N):
		C, F, X = [float(x) for x in stdin.readline().split()]
		t = minimize_time(C, F, X)
		print "Case #%d:" % (i+1), t
