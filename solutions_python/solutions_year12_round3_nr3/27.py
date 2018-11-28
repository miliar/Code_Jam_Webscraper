#!/usr/bin/env python
import math

def process_file(file):
	fsock = open(file)
	text = fsock.read()
	fsock.close()
	lines = text.split('\n')
	return lines


def process_lines(lines):
	ans = []
	first = True
	N = -1
	for line in lines:
		if first == True:
			first = False
		elif N == -1:
			if line != '':
				case = {}
				N = -1
				M = -1
				A = []
				B = []
				for num in line.split(' '):
					if N == -1:
						N = int(num)
					elif M == -1:
						M = int(num)
				case['N'] = N
				case['M'] = M
			else:
				return ans
		elif len(A) == 0:
			toggle = False
			cur = []
			for num in line.split(' '):
				cur.append(int(num))
				if toggle:
					A.append((cur[0], cur[1]))
					toggle = False
					cur = []
				else:
					toggle = True
			case['A'] = A
		elif len(B) == 0:
			toggle = False
			cur = []
			for num in line.split(' '):
				cur.append(int(num))
				if toggle:
					B.append((cur[0], cur[1]))
					toggle = False
					cur = []
				else:
					toggle = True
			case['B'] = B
			ans.append(case)
			N = -1
	return ans

def process_case(line):
	N = line['N']
	M = line['M']
	A = line['A']
	B = line['B']
	return best(A, B)

def best(A, B):
	if len(A) == 0 or len(B) == 0:
		return 0
	firstA = A[0]
	firstB = B[0]
	if firstA[1] == firstB[1]:
		if firstA[0] == firstB[0]:
			return firstA[0] + best(A[1:], B[1:])
		elif firstA[0] < firstB[0]:
			newB = B[:]
			newB[0] = (firstB[0] - firstA[0], firstB[1])
			return firstA[0] + best(A[1:], newB)
		else:
			newA = A[:]
			newA[0] = (firstA[0] - firstB[0], firstA[1])
			return firstB[0] + best(newA, B[1:])
	else:
		return max(best(A[1:], B), best(A, B[1:]))

if __name__ == "__main__":
	import sys
	filename = sys.argv[1]
	lines = process_file(filename)
	lines = process_lines(lines)
	c = 0
	for line in lines:
		#print line
		c += 1
		print "Case #%d: %s" % (c, process_case(line))