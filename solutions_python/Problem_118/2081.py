#!/usr/bin/env python

import sys
import math

def checkPalin(num):
	numList = list(str(num))
	palin = True
	while len(numList) > 1:
		if numList.pop(0) != numList.pop():
			palin = False
			break
	
	return palin

def checkNum(num):
	palin2 = True	
	square = False
	
	root = math.sqrt(num)
	
	if int(root + 0.5) ** 2 == num:
		square = True
		palin2 = checkPalin(int(root + 0.5))


	return (square and palin2)

def main():
	inp = sys.argv[1]
	out = sys.argv[2]

	fhInp = open(inp)
	fhOut = open(out, 'w')
	num = int(fhInp.readline().strip())
	
	for i in range(num):
		fhOut.write("Case #" + str(i+1) + ": ")
		line = fhInp.readline().strip().split(' ')
		A = int(line[0])
		B = int(line[1])

		count = 0
		while A <= B:
			num = A
			A += 1
			if not checkPalin(num):
				continue

			if checkNum(num) == True:
				count += 1


		fhOut.write(str(count) + "\n")



if __name__ == "__main__":
	main()
