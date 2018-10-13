import numpy as np
import math
def mainFunc(N, R, O, Y, G, B, V):
	ret = ""
	S = [(R,'R'),(Y,'Y'),(B,'B')]
	S = sorted(S)
	s0,s1,s2 = S[0][0],S[1][0],S[2][0]
	if(s2>N/2): return "IMPOSSIBLE"
	for i in range(s1-s0):
		ret+=S[2][1]+S[1][1]
	for i in range((s2-s1+s0)/2):
		ret+=S[2][1]+S[1][1]+S[2][1]+S[0][1]
	if((s2-s1+s0)%2==1): ret+=S[2][1]
	for i in range(s0-((s2-s1+s0)/2)):
		ret+=S[1][1]+S[0][1]
	return ret
		
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(int(P[0]), int(P[1]),int(P[2]), int(P[3]),int(P[4]), int(P[5]), int(P[6]))