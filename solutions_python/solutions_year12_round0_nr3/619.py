# Katja Collier
# Google Code Jam 2012, Qualification Problem C: Recycled Numbers

import sys

''' Outline:
iterate through every possible "n" value :
	count number of distinct "m" values that are greater than
	n and <= B, add to overall counter
'''
	
file = sys.stdin
lines = []
for l in file :
	lines.append(l)

k = 1
while k < len(lines) :
	case = map(int, lines[k].split())
	A = case[0]
	B = case[1]
	counter = 0

	n = A
	while n <= B :
		numString = str(n)
		j = 0
		mList = []
		while j < len(numString) :
			newString = numString[j:] + numString[:j]
			m = int(newString)
			if m > n and m <= B :
				if [n, m] not in mList :
					mList.append([n, m])
			j += 1
		counter += len(mList)
		n += 1

	
	
	print "Case #%d: %d" % (k, counter)
	k += 1












'''def numPairs(num) :
	numString = str(num)
	count = 0
	i = 1
	while i < len(numString) :
		newString = numString[i:] + numString[:i]
		if newString == numString :
			count += 1
		i += 1
	return count
	
print numPairs(

input = sys.stdin
j = 0

for line in input :
	if j != 0 :
		counter = 0
		line = line.split()
		num = int(line[0])
		while num <= int(line[1]) :
			counter += numPairs(num)
			num += 1
		print "Case #%d: %d" % (j, counter)
	j += 1'''