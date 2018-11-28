import numpy as np
def mainFunc(S, K):	
	ret = 0
	for i in range(len(S)-K+1):
		if S[i]=="-":
			ret+=1
			for j in range(K):
				if S[i+j]=='-': S[i+j]='+'
				else: S[i+j]='-'
	for i in range(K):
		if S[len(S)-1-i]=='-': return "IMPOSSIBLE"
	return str(ret)
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(list(P[0]), int(P[1]))