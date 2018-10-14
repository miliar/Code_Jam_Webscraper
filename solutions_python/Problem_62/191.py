# coding: utf8

import os, sys, re, string

def is_intersect(line1, line2):
	return ((line1[0] > line2[0]) and (line1[1] < line2[1])) or ((line1[0] < line2[0]) and (line1[1] > line2[1]))

def main():
	T = int(sys.stdin.readline())
	for index in xrange(1, T+1):
		N = int(sys.stdin.readline())
		points = [map(int, sys.stdin.readline().split(" ")) for i in xrange(N)] 
		if N == 1:
			print "Case #%d: 0" % index
		else:
			count = 0
			for i in xrange(1,N):
				for j in xrange(i):
					if is_intersect(points[i], points[j]):
						count += 1
			print "Case #%d: %d" % (index, count)


if __name__ == '__main__':
	main()


