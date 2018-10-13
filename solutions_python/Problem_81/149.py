#!/usr/bin/env python
import sys
import re
from sets import Set


def main():
	T = raw_input()
	for t in range(int(T)):
		NN = []
		WP = []
		OWP = []
		OOWP = []
		N = int(raw_input())
		for i in range(N):
			NN.append(list(raw_input()))

		for i in range(N):
			SS = 0
			NS = 0
			for j in range(N):
				if(NN[i][j] == '1'):
					NS += 1;
					SS += 1;
				elif(NN[i][j] == '0'):
					NS +=1;
			WP.append((SS+0.0)/NS)

		for i in range(N):
			RR = 0
			NR = 0
			for j in range(N):
				SS = 0
				NS = 0
				if NN[i][j] == '.':
					continue
				for k in range(N):
					if k == i:
						continue
					if(NN[j][k] == '1' ):
						NS += 1;
						SS += 1;
					elif(NN[j][k] == '0'):
						NS +=1;
				RR += (SS+0.0)/NS;
				NR += 1
			OWP.append((RR+0.0)/NR)

		for i in range(N):
			RR = 0
			NR = 0
			for j in range(N):
				if j == i:
					continue
				if NN[i][j] == '.':
					continue
				RR += OWP[j]
				NR += 1
			OOWP.append((RR+(0.0))/NR)
			
		print "Case #%d:" % (1+t)
		for i in range(N):
			print 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]

if __name__ == "__main__":
    main()
