#!/usr/bin/env python
import sys
import re
from sets import Set


def main():
	T = raw_input()
	for t in range(int(T)):
		Y,X = map(int, raw_input().split())
		NN = []
		MM = []
		for y in range(Y):
			L = list(raw_input())
			NN.append(L)
			MM.append(L[:])
		
		I = False
		for y in range(Y):
			for x in range(X):
				if(NN[y][x] == '#'):
					if(y<Y-1 and x < X-1 and NN[y+1][x] == '#' and NN[y][x+1] == '#' and NN[y+1][x+1] == '#'):
						NN[y][x] = '/'
						NN[y][x+1] = '\\'
						NN[y+1][x] = '\\'
						NN[y+1][x+1] = '/'
					else:
						I = True
						break

		print "Case #%d:" % (1+t)
#		for y in range(Y):
#			S = ""
#			for x in range(X):
#				S += str(MM[y][x])
#			print S

		if I:
			print "Impossible"
		else:
			for y in range(Y):
				S = ""
				for x in range(X):
					S += str(NN[y][x])
				print S


if __name__ == "__main__":
    main()
