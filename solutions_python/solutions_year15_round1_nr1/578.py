#!/usr/bin/python

import sys

def solveMushrooms(mushrooms):
	# method 1
	x = 0
	last = 0
	for m in mushrooms:
		if m<last:
			x += last-m
		last = m
	# method 2
	rate = 0
	for i in range(len(mushrooms)-1):
		r = mushrooms[i] - mushrooms[i+1]
		rate = max(r, rate)
	y = 0
	prev = mushrooms[0]
	for m in mushrooms[1:]:
		y += min(rate, prev)
		prev = m
	return x, y

def main():
	numTests = int(sys.stdin.readline())
	for n in range(numTests):
		N = sys.stdin.readline().strip()
		mushrooms = sys.stdin.readline().strip().split(' ')
		N = int(N)
		mushrooms = [int(m) for m in mushrooms]
		x, y = solveMushrooms(mushrooms)

		print "Case #%d: %d %d" % (n+1, x, y)

if __name__ == "__main__":
    main()

