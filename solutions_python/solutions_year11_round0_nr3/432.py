#!/usr/bin/python
import sys

def binaryAdd(int1, int2):
	bin1 = bin(int1)[2:]
	bin2 = bin(int2)[2:]
	larger = ''
	smaller = ''
	if len(bin1) != len(bin2): # balance 2 strings to same size
		if len(bin1) > len(bin2):
			larger = bin1
			smaller = bin2
		else:
			larger = bin2
			smaller = bin1
		difference = len(larger)-len(smaller)
		for i in range(0, difference):
			smaller = '9' + smaller
	else:
		larger = bin1
		smaller = bin2
	output = ''
	for index in range(0, len(larger)):
		if larger[index] == smaller[index]:
			output += '0'
		elif smaller[index] == '9':
			output += larger[index]
		else:
			output += '1'
	return int(output, 2)
	
def cry(list1, list2):
	total1 = -1
	total2 = -1
	for item in list1:
		if total1 == -1:
			total1 = item
		else:
			total1 = binaryAdd(item, total1)
	for item in list2:
		if total2 == -1:
			total2 = item
		else:
			total2 = binaryAdd(item, total2)
	return total1 != total2
	

data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	sys.stdout.write("Case #%d: " % case)
	N = int(data.pop(0)) #no. of candies
	line = data.pop(0)
	answer = 'NO'
	
	sean = []
	patrick = []

	for item in line.split():
		sean.append(int(item))
	sean.sort(reverse=True)
	
	patrick.append(sean.pop(-1))
	while len(sean) > 0:
		if cry(sean, patrick):
			patrick.append(sean.pop(-1))
		else:
			answer = str(sum(sean))
			break

	sys.stdout.write(answer + "\n")
	case += 1

	
	
	