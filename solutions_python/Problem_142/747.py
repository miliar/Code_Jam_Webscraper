#/usr/bin/python

import sys
import math

t = int(sys.stdin.readline())

def findMean(arr):
	x = sum(arr) / float(len(arr))
	r = int((x+0.5))

	s1 = 0
	for i in range(len(arr)):
		s1 += int(math.fabs(r-arr[i]))

	return s1

	# tt = sum(arr)
	# x = int(round(tt/len(arr)))
	# s1 = 0
	# for i in range(len(arr)):
	# 	s1 += int(math.fabs(x-arr[i]))
	# if (x*len(arr) < tt):
	# 	x+=1
	# 	s2 = 0
	# 	for i in range(len(arr)):
	# 		s2 += int(math.fabs(x-arr[i]))
	# 	if (s2 < s1):
	# 		s1 = s2
	# return s1

for ii in range(t):
	n = int(sys.stdin.readline())

	m = []
	for i in range(n):
		x = sys.stdin.readline().rstrip()
		m.append(x)
	
	chars = []
	chars.append(m[0][0])
	for i in range(1,len(m[0]),1):
		if (m[0][i-1] != m[0][i]):
			chars.append(m[0][i])

	possible = True
	counts = [[0 for j in range(n)] for i in range(len(chars))]
	for i in range(n):
		if (not possible):
			break
		index = 0
		if (m[i][0] != chars[index]):
			possible = False
			break
		else:
			counts[index][i] += 1
			for j in range(1,len(m[i]),1):
				if (m[i][j-1] != m[i][j]):
					index += 1
					if (index >= len(chars)):
						possible = False
						break
					if (m[i][j] != chars[index]):
						possible = False
						break
					counts[index][i] += 1
				else:
					counts[index][i] += 1
			if (index < len(chars)-1):
				possible = False
				break

	if possible:
		result = 0
		for i in range(len(chars)):
			result += findMean(counts[i])
	else:
		result = "Fegla Won"
	print "Case #{0:0d}:".format(ii+1), result
