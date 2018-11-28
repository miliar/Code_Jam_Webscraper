#!/usr/bin/env python
import sys

def main():
	T = int(raw_input())
	for j in range(int(T)):
		I = map(int,raw_input().split());
		N = I[0]
		S = I[1]
		P = I[2]
		T = I[3:]
		if(P >= 2):
			UU = P*3-2
			UL1 = P*3-1-2
			UL2 = P*3-2-2
		else:
			UU = P*3-1
			UL1 = -1;
			UL2 = -1;
		
		A = 0
		B = 0
		
		for i in range(N):
			if(T[i] >= UU):
				A = A + 1
			if((T[i] == UL1) or (T[i] == UL2)):
				B = B + 1
				
		print "Case #"+str(j+1)+": "+str(A+min(B, S))
		

if __name__ == "__main__":
    main()
