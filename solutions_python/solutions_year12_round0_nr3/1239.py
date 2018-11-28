'''
Created on Apr 14, 2012

@author: maka6er
'''

import math

def isRecycledPair(number1, number2):
	n1 = int(math.log10(number1)) + 1
	n2 = int(math.log10(number2)) + 1
	
	if n1 == n2:
		for i in range(1, n1):
			p = pow(10, i)
			right = number1 % p
			left = (number1  - right) / p
			number = right * pow(10, n1 - i) + left
			if number == number2:
				return True
    
	return False

#===============================================================================
#input

T = 0
lines = []
input_file = open('Recycled_Numbers.input', 'r')
input_file_lines = input_file.readlines()
T = int(input_file_lines[0])
line_number = 0
for line in input_file_lines:
    if line_number > 0:
        tmp = line.rstrip('\n').split(' ')
        lines.append([int(tmp[0]), int(tmp[1])])
    line_number += 1
    if line_number > T:
        break    

#===============================================================================

results = []

for line in lines:
	result = 0
	for i in range(line[0], line[1]):
		for j in range(i + 1, line[1] + 1):
			if isRecycledPair(i, j):
				result += 1
	results.append(result)

i = 1
for result in results:
	print 'Case #' + str(i) + ': ' + str(result)
	i += 1
#===============================================================================
