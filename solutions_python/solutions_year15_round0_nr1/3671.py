# A: Standing ovation

import sys, os

t = int(sys.stdin.readline())

def solve(maxS, people_str):
	my_sum = 0
	needed = 0
	for idx, char in enumerate(people_str):
		if my_sum >= idx and int(char) != 0:

			my_sum += int(char)
		elif int(char) != 0:
			needed += idx - my_sum
			my_sum += needed + int(char)
	return needed

for i in xrange(t):
	maxS, people_str = sys.stdin.readline().strip().split()
	print "Case #"+str(i+1)+": "+str(solve(maxS, people_str))












