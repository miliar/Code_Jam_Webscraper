from sys import * 
import os
import string
import math

def countSteps(arr1, arr2):
	ar_turns_a = []
	ar_turns_b = []
	
	# fill arr
	pos_a = 1
	pos_b = 1
	for i in range(len(arr1)):
		if (arr1[i] != 0):
			required = abs(arr1[i] - pos_a) + 1
			ar_turns_a.append(required)
			pos_a = arr1[i]
			
			if (sum(ar_turns_a) < sum(ar_turns_b)):
				ar_turns_a.append(sum(ar_turns_b) - sum(ar_turns_a))
			if (sum(ar_turns_a) == sum(ar_turns_b)):
				ar_turns_a.append(1)
			
		elif (arr2[i] != 0):
			required = abs(arr2[i] - pos_b) + 1
			ar_turns_b.append(required)
			pos_b = arr2[i]
			
			if (sum(ar_turns_b) < sum(ar_turns_a)):
				ar_turns_b.append(sum(ar_turns_a) - sum(ar_turns_b))
			if (sum(ar_turns_b) == sum(ar_turns_a)):
				ar_turns_b.append(1)
			
	if sum(ar_turns_a) > sum(ar_turns_b):
		return sum(ar_turns_a)
	return sum(ar_turns_b)


# open file
f = open("input.txt", "r")
numlines = int(f.readline())

# iterate through lines
num = 0
for line in f: 
	num += 1
	l = line.replace('\n', '').split(' ')
	num_tests = int(l[0])
	a = []
	b = []
	for i in range(1, num_tests + 1): # 1,2,3
		if l[i * 2 - 1] == 'O':
			# orange
			a.append(int(l[i * 2]))
			b.append(0)
		elif l[i * 2 - 1] == 'B':
			# blue
			a.append(0)
			b.append(int(l[i * 2]))
	# find max way
	print 'Case #' + str(num) + ': ' + str(countSteps(a, b))
		
