#!/usr/bin/env python

def solve(temp):
	N,K = temp
	if K == 0:
		return "OFF"
	K = K % 2 ** N
	return "ON" if K == 2**N -1 else "OFF"

def solveFile(Filename):
	inFile = file(Filename, "r")
	outFile = file(Filename[:-2]+"out", "w")
	L = int(inFile.readline())
	for i, line in enumerate(inFile.readlines(),1):
		outFile.write("Case #%i: %s\n" %(i, solve([int(i) for i in line.split()])))

#print solve(1,0)
#print solve(1,1)
#print solve(4,0)
#print solve(4,47)

#solveFile("/home/king/scripts/python/google codejam/temp/A-small-attempt0.in")
solveFile("/home/king/scripts/python/google codejam/temp/A-large.in")

