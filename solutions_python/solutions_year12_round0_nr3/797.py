#!/usr/bin/env python
import sys
import math
from sets import Set

def ev(X, R, W, F, T):
	M = 10
	S = Set()
	for i in range(R-1):
		P = (X%M)*W+X/M
		if(P>=F and P<=T):
			if(P > X):
				S.add(P)
		M,W = M * 10, W / 10
	return len(S)
	
def main():
	T = int(raw_input())
	for j in range(int(T)):
		F,T = map(int,raw_input().split());
		R = int(math.ceil(math.log(T,10)))
		W = int(math.pow(10, R-1))
		S = 0;
		for i in range(F,T+1):
			S += ev(i,R,W,F,T);
		print "Case #"+str(j+1)+": "+str(S)
		

if __name__ == "__main__":
    main()
