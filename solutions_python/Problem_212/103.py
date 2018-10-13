from math import floor
from math import ceil

def f(grouplist,packsize):
	if packsize == 2:
		return f2(grouplist)
	if packsize == 3:
		return f3(grouplist)
	else:
		return f4(grouplist)

def f2(grouplist):
	count = [0,0]
	for n in grouplist:
		count[n % 2] += 1
	return int(count[0] + ceil(count[1]/2))

def f3(grouplist):
	count = [0,0,0]
	for n in grouplist:
		count[n % 3] += 1
	output = count[0] + min(count[1],count[2]) + floor(abs(count[1]-count[2]) / 3)
	if (count[1] - count[2]) % 3 != 0:
		output += 1
	return output
	
def f4(grouplist):
	count = [0,0,0,0]
	for n in grouplist:
		count[n % 4] += 1
	left1 = count[1]
	left2 = count[2]
	left3 = count[3]
	# 0 singles
	output = count[0]
	# 13 pairs
	m13 = min(left1,left3)
	output += m13
	left1 -= m13
	left3 -= m13
	# 22 pairs
	m22 = left2 // 2
	output += m22
	left2 -= 2*m22
	# 211 triples
	if left2 == 1 and left1 >= 2:
		output += 1
		left2 -= 1
		left1 -= 2
	# 211 triples
	if left2 == 1 and left3 >= 2:
		output += 1
		left2 -= 1
		left3 -= 2
	# quadruples
	output += max(left1,left3) // 4
	# incomplete groups at end
	if (1*count[1]+2*count[2]+3*count[3]) % 4 != 0:
		output += 1
	return output

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		grouplength,packsize = [int(x) for x in inputLines.pop(0).rstrip().split()]
		grouplist = [int(x) for x in inputLines.pop(0).rstrip().split()]
		fileOUT.write('Case #' + str(num+1) + ': ' + str(f(grouplist,packsize)) + '\n')