#!/usr/bin/python

import sys

def Dec2Bin(N, bits):
	Q = 1
	R = 1
	STR = ''
	if N == 0:
		return '0'
	while Q != 0:
		Q = N / 2
		R = N % 2
		STR = str(R) + STR
		N = Q
	for i in range(len(STR), bits):
		STR = "0"+STR
	return STR

testIn = open(sys.argv[1], "r")
testOut = open(sys.argv[2], "w")
nbTests = int(testIn.readline())


for nbTest in range(1,nbTests+1):
	line = testIn.readline()[:-1]
	line = line.split(" ")
	nbBits = int(line[0])

	val = int(line[1])%(pow(2,nbBits))
	binary = Dec2Bin(val, nbBits)
	outLine = ""
	on = True
	for bit in binary:
		if bit == "0":
			outLine =  "Case #"+str(nbTest)+": OFF"
			on = False
	if on:
		outLine = "Case #"+str(nbTest)+": ON"
	print outLine
	testOut.write(outLine+"\n")

testIn.close()
testOut.close()
