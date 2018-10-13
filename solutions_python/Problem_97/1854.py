import os
import sys

def hasRecycle(n, m):
	if len(n) != len(m):
		return False
	for i in range(len(n)):
		if n[i] == m[0]:
			swap = n[i:]+n[:i]
			if swap == m:
				return True
	return False



f = open('C-small-attempt2.in')
s = f.read()

s = s.split('\n')
T = int(s[0])

for case in range(T):
	[A, B] = s[case+1].split(' ')
	A = int(A)
	B = int(B)
	num = 0
	for i in range(A, B):
		for j in range(i+1, B+1):
			if hasRecycle(str(i), str(j)):
				num += 1
	print "Case #"+str(case+1)+": "+str(num)
