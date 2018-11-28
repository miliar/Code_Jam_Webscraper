import numpy as np
import random
def mainFunc(N, M):
	ret = '';
	V = np.zeros(N)
	J_o = -1
	qt = 0
	for i in range(M):
		P = raw_input().split(' ')
		K = P[0]
		J = int(P[2])-1
		if(K=='o' or K=='x'): J_o = J
		if(K=='x'): ret+="\no 1 "+str(J+1)
		V[J] = 1
	if J_o==-1:
		ret+="\no 1 1"
		J_o = 0
		V[0] = 1
		
	for i in range(N):
		if V[i]==0: ret+="\n+ 1 "+str(i+1)
		if i<J_o: ret+="\nx "+str(N-i)+" "+str(i+1)
		if i>J_o: ret+="\nx "+str(i-J_o+1)+" "+str(i+1)
		if i>0 and i<N-1: ret+="\n+ "+str(N)+" "+str(i+1)
	return str(max(N*3-2,2))+" "+str(len(ret.split('\n'))-1)+ret

T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' + mainFunc(int(P[0]),int(P[1]))
	