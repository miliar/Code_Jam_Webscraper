from math import floor, ceil, pi
from collections import Counter
import numpy as np

o = ""
cases = []

with open("A-small-attempt2.in", "r") as input:
	T = int(input.readline())
	for t in range(T):
		# print(t)
		S = []
		N,K = map(int, input.readline().split()) # N ingredients and P packages
		R = []
		H = []
		RH = []
		for i in range(N):
			Ri,Hi = map(int, input.readline().split())
			R.append(Ri)
			H.append(Hi)
			RH.append([i,Ri,Hi])
		
		
		
		Rmax = 0
		for k in range(K):
			ofRmax = max(RH, key = lambda x: max((x[1]**2)-(Rmax**2),0)+2*x[1]*x[2])
			# print(ofRmax)
			if k == 0:
				Rmax = ofRmax[1]
			S.append(ofRmax)
			# print(RH)
			RH[ofRmax[0]] = [ofRmax[0], 0, 0]
		# print(S)
		s = 0
		Rmax = max(S, key = lambda x: x[1])[1]
		
		s = pi*(Rmax**2)+sum([2*pi*S[i][1]*S[i][2] for i in range(K)])
		s = round(s,9)
		print("Case #" + str(t+1) + ":", s)
		
	# q =  pi*(9**2)+2*pi*9*3+ 2*pi*8*4
	# print(q)

# print(o)
	
# with open("output.txt", "w") as output:
	# output.write(o)
	