#! /usr/bin/env python

import sys
import math

fair_and_squares = []

def preload():
	low_sqrt = int(math.ceil(math.sqrt(float(1))))
	high_sqrt = int(math.floor(math.sqrt(float(100000000000000))))
	cnt = 0
	for i in range(low_sqrt, high_sqrt + 1):
		i_str = str(i)
		il = list(i_str)
		ilr = il[:]
		ilr.reverse()
		if il == ilr:
			i_sq_str = str(i * i)
			isl = list(i_sq_str)
			islr = isl[:]
			islr.reverse()
			if (isl == islr):
				fair_and_squares.append(i * i)
				
def analyze(low, high):
	cnt = 0
	for i in fair_and_squares:
		if i > float(high):
			break
		if i >= float(low):
			cnt += 1
	return cnt
	

def main():
	preload()
	cases = int(sys.stdin.readline().rstrip())
	for case in range(1, cases + 1):
		(low, high) = sys.stdin.readline().rstrip().split()
		print "Case #%d: %d" % (case, analyze(low, high))

if __name__ == "__main__":
	main()