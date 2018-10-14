#!/usr/bin/python3

t = int(input())

for testcase in range(t): 
	n = [int(i) for i in list(input())]
	pending = 0
	for i in range(len(n)-1):
		if n[i] > n[i+1]: 
			n[i-pending] = n[i-pending] - 1
			for j in range(i-pending+1, len(n)):
				n[j] = 9
			break
		elif n[i] == n[i+1]: pending += 1
		else: pending = 0

	import re
	print("Case #" + str(testcase+1) + ": " + re.sub('^0*', '', ''.join(str(i) for i in n)))
