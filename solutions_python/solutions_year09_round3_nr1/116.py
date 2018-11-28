#!/usr/bin/python

def doCase():
	X = raw_input();
	D = {}
	L = 0;
	if len(X) == 1:
		return 1;
	
	for j in range(len(X)):
		if not D.has_key(X[j]):
			D[X[j]] = -1;
			
	L = len(D);
	if L<2:
	    L = 2;
	
	D[X[0]] =  1;
	
	for i in range(len(X)):
		if D[X[i]] == -1:
			D[X[i]] = 0;
			break;
	k = 2;
	for i in range(1,len(X)):
		if D[X[i]] == -1:
			D[X[i]] = k;
			k += 1;
	S = 0;
	for j in range(len(X)):	
		S *= L;
		S += int(D[X[j]])
	return S;
		

N = input()

for i in range(N):
	print "Case #"+str(i+1)+": " +str(doCase());
				
	
	

	
