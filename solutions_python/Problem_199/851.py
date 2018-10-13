#!/bin/python
import sys

def allHappy(stk):
	for i in stk:
		if (i == '-'):
			return False
	return True

n = int(raw_input().strip())
for cnt in range(n):
	u, v = raw_input().strip().split(" ")
	v = int(v)
	u = list(u)
	flag = False
	flip = 0
	for i in range(len(u)):
		if (u[i] == '-'):
			if (len(u) - i < v):
				flag = True
				break
			flip += 1
			for j in range(v):
				if (u[i + j] == '-'):
					u[i + j] = '+'
				else:
					u[i + j] = '-'
	if (flag):
		print ("Case #{}: {}".format(cnt + 1, "IMPOSSIBLE"))
	else:
		print ("Case #{}: {}".format(cnt + 1, flip))
