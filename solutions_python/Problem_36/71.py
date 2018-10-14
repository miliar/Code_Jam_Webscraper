#!/usr/bin/env python
import sys

search = "welcome to code jam"

def main():
	n = int(sys.stdin.readline().strip())
	for i in range(n):
		test = sys.stdin.readline().strip()
		#print "TEST: " + test
		print "Case #%d: %04d" % (i+1, countSubsequences(test))

def countSubsequences(sequence):
	positions = []
	for letter in search:
		letter_positions = []
		for pos, l in enumerate(sequence):
			if l == letter:
				letter_positions.append(pos)
		positions.append(letter_positions)
	positions.reverse()

	tallies = []
	tallies.append([1 for pos in positions[0]])

	for i in range(1, len(positions)):
		tallies.append([sum(tallies[i-1][start(positions[i-1], pos):])%10000 for pos in positions[i]])

	#print tallies

	return sum(tallies[-1])%10000
	
def start(ns, target):
	for i, n in enumerate(ns):
		if target < n:
			return i
	return len(ns)

main()

