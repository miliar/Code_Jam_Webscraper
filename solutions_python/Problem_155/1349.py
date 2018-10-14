#!/usr/bin/python

import sys

def solveShyness(maxShyness, shyness):
	answer = 0
	total = 0
	for i, s in enumerate(shyness):
		if i>total :
			a = i-total
			answer = max(answer, a)
		total += s
	return answer

def main():
	f = open("input.txt")
	numTests = int(f.readline())
	output = ""
	for i in range(numTests):
		[maxShyness, shyness] = f.readline().split(' ')
		maxShyness = int(maxShyness)
		shyness = [int(c) for c in shyness if c!='\n']

		answer = solveShyness(maxShyness, shyness)
		if answer != None:
			output += "Case #" + str(i+1) + ": " + str(answer) + '\n'
		else:
			output += "Case #" + str(i+1) + ": NOT POSSIBLE\n"

	fout = open("output.txt", "w")
	fout.write(output)

if __name__ == "__main__":
    main()

