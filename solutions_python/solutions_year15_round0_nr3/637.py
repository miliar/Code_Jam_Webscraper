import sys
import fileinput
import re

#fileio
#fileName = 'C-large'
fileName = 'C-small-attempt0'
#fileName = 'C-test'
input = fileName + ".in"
output = fileName + ".out"

i = 2
j = 3
k = 5

def multiply(a, b):
	minus = -1 if a < 0 else 1
	a = a * minus
	r = 7
	if a == b: 
		if a == 1: r = 1
		else: r = -1
	if a == 1: r = b
	if a == i:
		if b == j: r = k
		if b == k: r = -j
	if a == j:
		if b == i: r = -k
		if b == k: r = i
	if a == k:
		if b == i: r = j
		if b == j: r = -i
	return r * minus

###
with open(input) as fi, open(output, "w") as fo:
	count = 0
	content = fi.readlines()[1:]
	for l in range(len(content)/2):
		result = 0
		ll, r = content[l*2].strip().split(' ')
		s = content[l*2+1].strip()*int(r)
		current = 1
		passed = 0
		###
		for x in s:
			current = multiply(current, eval(x))
			if current == i and passed == 0:
				current, passed = 1, 1
			if current == j and passed == 1:
				current, passed = 1, 2
			if current == k and passed == 2:
				current, passed = 1, 3
		print current, passed
		if current == 1 and passed == 3: result = 'YES'
		else: result = 'NO'
		###
		#normal
		count += 1
		resultStr = "Case #"+str(count)+": "+str(result)
		print resultStr
		fo.write(resultStr+'\n')

