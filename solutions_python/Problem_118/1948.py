import sys
import math

output = open('output.out', 'w')
File = open(sys.argv[1], 'r')

count = 0

def isPal(number):
	number = str(number)
	if len(number) == 1:
		return True
	revNum = number[::-1]
	return number == revNum

def isSquare(number):
	if(number == 1):
		return True
	root = int(math.sqrt(number))
	return number == int(math.pow(root, 2)) and isPal(root)

def parse(head, tail, count):
	passNum = 0
	for item in range(head, tail + 1):
		if isPal(item):
			if isSquare(item):
				passNum = passNum + 1
	# print passNum, count
	head = "Case #"+str(count)+": "
	global output
	output.write(head + str(passNum) + "\n")

for line in File:
	if not line.strip():
		continue
	else:
		if count != 0 and count <= 100:
			tmp = line.strip().split(" ")
			if int(tmp[0]) >= 1 and int(tmp[1]) <= 1000:
				parse(int(tmp[0]), int(tmp[1]), count)
		count = count + 1
		
File.close()
output.close()