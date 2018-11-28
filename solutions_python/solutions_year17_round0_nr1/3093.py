import sys
import numpy as np
input = sys.stdin.readlines()

def flipping(S, K):
	S = list(S)
	num_flip = 0
	for start in range(len(S) - K + 1):
		# print S
		if S[start] == '-':
			# print S[start:start+K]
			num_flip+=1		
			for i in range(start,start+K,1):
				if S[i] == '+':
					S[i] = '-'
				else:
					S[i] = '+'
			# print "flipped",S[start:start+K]
		# print
	
	if '-' in S[(len(S) - K + 1):]:
		return "IMPOSSIBLE"

	else:
		return str(num_flip)



for i in range(1,len(input),1):
	elem = input[i]
	in_line = elem.split()
	S = in_line[0]
	K = int(in_line[1])
	
	output = "Case #" + str(i) + ": " + flipping(S, K)
	print output