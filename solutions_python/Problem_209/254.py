import itertools
import math

def all_smallest(pancakes, x):
	area = pancakes[x][0]
	for i in xrange(len(pancakes)):
		pan = pancakes[i]
		if(pan[0] <= area):
			result = pancakes[i:]
			result.pop(x-i)
			return result
	return []

fd = open("in1.in", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out1", "w")

line_ind = 1
case = 1
while line_ind < len(lines):
	line  = lines[line_ind]
	fout.write("Case #" + str(case) + ": ")
	n = int(line.split()[0])
	k = int(line.split()[1])
	
	pancakes = []
	for i in xrange(n):
		line = lines[line_ind + 1 + i]
		panc = map(float, line.split())
		pancakes.append(panc)

	# Sort
	pancakes.sort(key=lambda x: -x[0])
	pancakes = sorted(pancakes, key = lambda x: (-x[0], -x[1]))

	# print n, k, pancakes

	# dyn = [[0 for j in xrange(n)] for i in xrange(k)]

	# print dyn

	# for i in xrange(k):
	# 	for j in xrange(n):

	old_pancakes = pancakes[:]
	best_result = -1
	for i in xrange(n):
		pancakes = old_pancakes[:]
		result = math.pi * (pancakes[i][0] **2) + pancakes[i][1] * (2*math.pi*pancakes[i][0])
		# print 1, pancakes
		pancakes = all_smallest(pancakes, i)
		# print 2, pancakes
		pancakes = sorted(pancakes, key = lambda x: -(x[0])*(x[1]))
		pancakes = pancakes[:k-1]
		# print 3, pancakes
		# print pancakes[:k-1]
		pancakes = sorted(pancakes, key = lambda x: -(x[0])*(x[1]))
		# print pancakes


		for pan in pancakes:
			result += pan[1] * (2*math.pi*pan[0])
		# print result

		if(result >= best_result):
			best_result = result

	print best_result
	fout.write(str(best_result) + "\n")

	case += 1
	line_ind += n + 1