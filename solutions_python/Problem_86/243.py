#!/usr/bin/python

import sys

def solve(cases):
	solution = []
	for case in cases:
		N = case[0]
		L = case[1]
		H = case[2]
		nums = case[3]
		ok = False
		for i in range(L,H + 1):
			total = 0
			for j in range(N):
				if nums[j] <= i and i % nums[j] == 0:
					total += 1
				if nums[j] > i and nums[j] % i == 0:
					total += 1
			if total == N:
				solution.append(str(i))
				ok = True
				break

		if not ok:
			solution.append("NO")
		
	return solution

f = open(sys.argv[1],'r')
caseCount = int(f.readline().strip('\n'))
cases = []
for i in range(caseCount):
	[N,L,H] = map(int,f.readline().strip('\n').split(' '))
	nums = map(int,f.readline().strip('\n').split(' '))
	cases.append((N,L,H,nums))

solution = solve(cases)

for i in range(len(solution)):
	print "Case #" + str(i + 1) + ": " + solution[i]
