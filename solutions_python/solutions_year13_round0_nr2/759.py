#!/usr/bin/env python2.7

MIN = 1
MAX = 100

def is_valid_point(lawn, x, y, height):
	# check if vertical line is valid
	line = 0
	line_length = len(lawn)
	for i in xrange(line_length):
		line += lawn[i][y]
	if line / height == line_length and line % height == 0:
		return True

	# check if horizontal line is valid
	line = 0
	line_length = len(lawn[x])
	for j in xrange(line_length):
		line += lawn[x][j]
	if line / height == line_length and line % height == 0:
		return True
	return False


def check_lawn(lawn, minimum, maximum):
	N = len(lawn)
	M = len(lawn[0])
	for height in xrange(minimum, maximum+1):
		for i in xrange(N):
			for j in xrange(M):
				if lawn[i][j] == height and not is_valid_point(lawn, i, j, height):
					print "Case #%d: NO" % (t+1)
					return
		
		for i in xrange(N):
			for j in xrange(M):
				if (lawn[i][j] == height):
					lawn[i][j] += 1
	print "Case #%d: YES" % (t+1)
	return

T = int(raw_input())

for t in xrange(T):
	lawn = []

	# get input in correct format...
	size = raw_input().split()
	N, M = int(size[0]), int(size[1])
	minimum = MAX
	maximum = MIN
	for n in xrange(N):
		heights = raw_input().split()
		for index in xrange(len(heights)):
			heights[index] = int(heights[index])
			if heights[index] < minimum:
				minimum = heights[index]
			if heights[index] > maximum:
				maximum = heights[index]
		lawn.append(heights)
		
	check_lawn(lawn, minimum, maximum)

