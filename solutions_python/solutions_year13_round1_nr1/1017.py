#!/usr/bin/python
import sys
import string
import math

squares = []

if len(sys.argv) != 2:
	print "Usage: bullseye.py <input file>"
	exit()

try:
	f = open( sys.argv[1], 'r' )
except:
	print "Could not open the file: " + sys.argv[1]
	exit()


def compute_area(r):
	#return areas[r+1]
	#return (r+1)*(r+1) - r*r
	return squares[r+1] - squares[r]


def compute_rings(r,t):

	num_rings = 0

	while t > 0:
		ml = compute_area(r)
		t = t - ml
		r = r + 2
		num_rings += 1

	if t == 0:
		return num_rings
	else: 
		return num_rings - 1

def compute_squares(max):
	i = 0
	while i <= max:
		squares.append( i*i )
		i += 1

num_tests = int(f.readline())

i = 0
compute_squares(1000)
while i < num_tests:
	test = map(int, string.split(f.readline(), ' '))
	y = compute_rings(test[0],test[1])
	print "Case #" + str(i + 1) + ": " + str(y)

	i += 1
