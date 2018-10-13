#!/usr/bin/python

def main():
	fin = open("small.in", "r")
	fout = open("output.txt", "w")

	firstline = 0

	for line in fin:
		if firstline != 0:
			line = line.split('/')
			first = int(line[0])
			second = int(line[1].strip())
			fout.write("Case #" + str(firstline) + ": " + str(test(first, second)) + '\n')

		firstline += 1

def test(first, second):
	import math
	from fractions import Fraction

	if first == 0:
		return "impossible"

	if second % 2 == 1:
		return "impossible"

	test =  str(Fraction(first, second)).split('/')
	first = test[0]
	second = test[1]

	if not math.log(float(second), 2).is_integer():
		return "impossible"
	
	per = float(first)/float(second)
	test = 1
	i = 0
	while (test > per):
		test = test * .5
		i += 1
	return i
	#print per
	#print math.log(second, 2)
main()
