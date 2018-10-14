#!/usr/bin/env python

def test():
	for i in range(1,300):
		for j in range(1,i):
			for k in range(1,j):
				t = solve([i,j,k])
				if t > 0 and t != brute([i,j,k]) :
					print i,j,k, brute([i,j,k]), solve([i,j,k])					

def brute(Numbers):
	t = 0
	temp = multiple(sorted(Numbers))
	while Numbers[0] % temp != 0 or Numbers[1] % temp != 0 or Numbers[2] % temp != 0:
		t += 1
		Numbers = [i + 1 for i in Numbers]
	return t

def gcd(a, b):
	if b > a:
		a, b = b, a
	while b > 0:
		temp = a % b
		if temp == 0:
			return b
		a, b = b, temp

def multiple(Numbers):
	#find the gcd of the multiple of the diffs
	diffs = [numTwo - num for i, num in enumerate(Numbers) for numTwo in Numbers[i+1:]]
	temp = diffs[0]
	for i in set(diffs):
		temp = gcd(temp, i)
		if temp == 1:
			return 1
	return temp

def solve(Numbers):
	Numbers = sorted(set(Numbers))
	timeBetween = multiple(Numbers)
	if timeBetween == 1:
		return 0
	temp = timeBetween - (min(Numbers) % timeBetween)
	return temp if temp != timeBetween else 0

def solveFile(Filename):
	inFile = file(Filename, "r")
	outFile = file(Filename[:-2]+"out", "w")
	int(inFile.readline())
	for i, line in enumerate(inFile.readlines(),1):
		outFile.write("Case #%i: %s\n" %(i, solve([int(i) for i in line.split()][1:])))

assert 4000000 == solve([26000000,11000000,6000000])
assert 0 == solve([1,10,11])
assert 99999999999999999999 == solve([800000000000000000001,900000000000000000001])
assert 4 == solve([11,26,41])
assert 2 == solve([1,4,7])

#solveFile("/home/king/scripts/python/google codejam/fair warning/B-small-test.in")
#solveFile("/home/king/scripts/python/google codejam/fair warning/B-small-attempt0.in")
solveFile("/home/king/scripts/python/google codejam/fair warning/B-large.in")
