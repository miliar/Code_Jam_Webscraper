#!/usr/bin/python
			
def next_permutation(X):
	for i in range(len(X)-1,0,-1):
		if X[i-1] < X[i]:
			j = len(X)-1;
			while X[j] <= X[i-1]:
				j-=1;
			
			X[i-1],X[j] = X[j],X[i-1]
			X = X[0:i] + X[i:][::-1]
			return True,X
	return False, X;


N = input();

def calcBX(P,X):
	R = [1 for _ in range(P)];
	S = 0
	for i in range(len(X)):
		R[X[i]] = 0;
		#print R;
		for k in range(X[i]-1,0-1,-1):
			if R[k] != 0:
				S += 1;
			else:
				break;
		#print "S1:"+str(S);
		for k in range(X[i]+1,P):			
			if R[k] != 0:
				S += 1;
			else:
				break;
		#print "S2:"+str(S);
	return S;

for XXX in range(N):
	P,Q = map(int, raw_input().split());
	X = map(int,raw_input().split());
	for i in range(len(X)):
		X[i] = X[i] -1;
	
	B = True;
	M = calcBX(P,X);

	while B:
		B,X = next_permutation(X);
		MM = calcBX(P,X);
		if MM < M:
			M = MM;
		#print "---"
		
	print "Case #"+str(XXX+1)+": "+str(M)
