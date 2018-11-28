import os
import sys
import numpy as np

def readFile(filename):
	fp = open(filename, 'r')
	T = int(fp.readline().strip())
	S = []
	for line in fp:
		l = line.strip().split(' ')
		S.append([l[0], int(l[1])])
	return T, S

def solve(S, K):
	n =  len(S)
	S = [S[i] for i in range(n)]
	count = 0
	for i in range(n-K+1):
		if S[i]=='-':
			count += 1
			for j in range(K):
				if S[i+j]=='-':
					S[i+j] = '+'
				else:
					S[i+j] = '-'
	flag = True
	print S
	for i in range(n-K, n):
		if S[i]=='-':
			flag = False
	if flag:
		return str(count)
	else:
		return "IMPOSSIBLE"
	
if __name__ == "__main__":
	filename = "A-large.in"
	T, S = readFile(filename)
	print T, S
	output = open("output.txt", 'w')
	for i in range(T):
		result = "Case #{}: {}".format(i+1, solve(S[i][0], S[i][1]))
		output.write(result)
		if not i==T-1:
			output.write('\n')
	output.close()
