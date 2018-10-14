#! /usr/bin/env python

"""
The following variables are used for the dimensions of the racquets:
fly: radius of the fly (f).
outer: Total radius of the racquet (R).
rim: Width of the rim (t).
gut: Radius of the strings (r).
gap: Side length of the gap between gut (g).
inner: Radius of the racquet, minus the rim and fly width (i.e.,
       the maximum distance the center of the fly could possibly
       be from the center of the racquet).
block: Size of a square block, see below.
sblock: Size of the ``safe'' block, that the fly can pass through.


By symmetry, this program only calculates the odds for 1/4th of the
racquet. The center will be the origin, and the quarter racquet will
occupy the first quadrant.

It works by adding up the areas of all the ``blocks''
between strings (referred to from now on as ``gut'' to avoid
confusion with the type). A diagram of a block:

Gut|        Gap        |Gut
|  |                   |  |
+-------------------------+
|                         |
|  +-------------------+  |
|  |                   |  |
|  |   +-----------+   |  |
|  |   |           |\  |  |
|  |   |           ||__|__|__ sblock (safe block)
|  |   |           ||  |  |
|  |   |           |/  |  |
|  |   +-----------+   |  |
|  |                }--|--|--  fly radius
|  +-------------------+  |
|                         |
+-------------------------+

The algorithm works as follows:
Overlay a square grid of blocks over the quarter-racquet large enough to
cover it. For each sblock, determine whether it is entirely within the inner
racquet (i.e., does not intersect the boundary of the rim), entirely outside
the racquet, or on the boundary. If it is on the boundary, determine how many
corners are outside, and from that, determine the ``safe'' area for the fly:

One corner:             Two corners:             Three corners:
 +---\--+         +------+         +-\----+         +------+
 |    \ |         |      |         |   \  |         \      |
 |     \|         ----__ |         |    | |         |\     |
 |      \         |     \_         |     ||         | \    |
 +------+         +------+         +-----|+         +--\---+

For each of these cases, some calculus was done by hand, yielding an expression
for the relevant area.

The safe areas are added up, and the resulting odds of the fly being hit
are calculated.
"""

from sys import argv
from math import *

# Functions to do the math.
def dist(x, y):
	"""Returns distance from the origin to a point."""
	return sqrt(x * x + y * y)

def rt(x, y):
	"""Self explanatory, used a ton calculating areas."""
	return sqrt(x * x - y * y)

def int_circ(rad, a, b, height):
	"""Integrates the area of a semicircle centered at the origin.
	The circle is of radius r, with integration performed from a to b.
	Then the area of the rectangle under the arc is subtracted, to give
	the area of the region."""
	def indef(x):
		rx = rt(rad, x)
		return (atan2(x, rx) * rad * rad + x * rx) / 2
	return indef(b) - indef(a) - height * (b - a)


def odds(dimstring):
	"""Calculate the odds that a given racquet will hit a fly."""
	dims = dimstring.split()
	# Names for each dimension:
	fly = float(dims[0])
	outer= float(dims[1])
	rim = float(dims[2])
	# Called gut, to avoid confusion with a certain OTHER type of string.
	gut = float(dims[3])
	gap = float(dims[4])
	# We calculate the area of 1/4th the circle.
	total_area = float(pi) * outer * outer / 4
	# Radius, discounting the rim.
	inner = outer - rim - fly
	# Now we just add up all the area that won't hit the fly.
	safe_area = 0
	def safe_block(rw, cl):
		# Side of one block:
		block = gap + 2 * gut
		# Side of one full safe block:
		sblock = gap - 2 * fly
		# Distances to the four corners of each sblock:
		# rw1-+--+
		#     |  |
		# rw0-+--+
		#      \  \_cl1
		#       \___cl0
		rw0 = rw * block + gut + fly
		rw1 = rw0 + sblock
                cl0 = cl * block + gut + fly
                cl1 = cl0 + sblock
		dists = [[0, 0], [0, 0]]
		dists[0][0] = dist(rw0, cl0)
		dists[0][1] = dist(rw0, cl1)
                dists[1][0] = dist(rw1, cl0)
                dists[1][1] = dist(rw1, cl1)
		# Now that we have the distances to each corner, we can
		# determine whether the sblock is in or out of the racket,
		# or on the edge.
		if (dists[0][0] >= inner):
			# Completely out of the racquet, no safe area.
			return 0
		elif (dists[1][1] <= inner):
			# Completely in the racquet, all safe area.
			return sblock * sblock
		elif ((dists[0][1] > inner) and (dists[1][0] > inner)):
			# Three corners out.
			if int_circ(inner, cl0, rt(inner, rw0), rw0) > sblock * sblock:
				print 1
			return int_circ(inner, cl0, rt(inner, rw0), rw0)
                elif ((dists[0][1] > inner) and (dists[1][0] <= inner)):
			# Two corners out:
			if int_circ(inner, rw0, rw1, cl0) > sblock * sblock:
				print 2
			return int_circ(inner, rw0, rw1, cl0)
                elif ((dists[0][1] <= inner) and (dists[1][0] > inner)):
			# Two corners out:
			if int_circ(inner, cl0, cl1, rw0) > sblock * sblock:
				print 3
			return int_circ(inner, cl0, cl1, rw0)
			# Note this is the same as the previous case, with
			# rows and columns interchanged.
                elif ((dists[0][1] <= inner) and (dists[1][0] <= inner)):
			# One corner out:
			return sblock * sblock + \
			int_circ(inner, rt(inner, rw1), cl1, rw1)
		else:
			# Just in case:
			return 0
		
	squares = int(ceil(inner / (gap + 2 * gut)))
	for rw in range(squares):
		for cl in range(squares):
			safe_area = safe_area + safe_block(rw, cl)
	return (1 - (safe_area / total_area))


if len(argv) != 3:
	print "Usage:", argv[0], "INPUT OUTPUT"
	exit(1)


input = open(argv[1], 'r')
output = open(argv[2], 'w')


numlines = int(input.readline())
for racquet in range(numlines):
	output.write('Case #' + str(racquet+1) + ': ')
	output.write(str(odds(input.readline())))
	output.write('\n')
