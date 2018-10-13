#!/usr/bin/python

import math

def area_concentric_circle(r):
	return (area_of_circle(r + 1) - area_of_circle(r))

def area_of_circle(r):
	return r**2 # multiple of PI

# Open file
fp = open('A-small-attempt0.in')
cases = int(fp.readline())
print '#Cases:', cases

# Open output file
fpout = open('output.txt', 'w')

for i in range(cases):
	[r, t] = [int(data) for data in fp.readline().split()]

	for N in xrange(1, t/2 + 1):
		area = 2*(r + 2*(N - 1)) + 1
		t -= area
#		print N, r, t, area
		if t <= 0:
			break
	
	if t < 0:
		N -= 1
		
	print 'Case #%d: %d' %(i + 1, N)
	fpout.write('Case #%d: %d\n' %(i + 1, N))