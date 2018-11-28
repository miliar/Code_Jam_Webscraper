#!/usr/bin/python
import fileinput
import sys
import numpy
import copy
import math

def prt(txt):
	sys.stdout.write(txt);



def main():
	count = int(raw_input())

	for c in range(0,count):
		prt("Case #" + str(c + 1)+": ")

		[As, Bs, Ks] = str.split(raw_input())
		(A, B, K) = (int(As), int(Bs), int(Ks))

		possiblePairs = []

		def findPossibles(a,b,k, values, depth):
			if k == 0 and a == 0 and b == 0:
				possiblePairs.append(values)		
				return		
			lastBit = k & 1;
			k = int(k / 2)
			a = int(a / 2)
			b = int(b / 2)
			if(lastBit == 0):
				if(values[0]+math.pow(2,depth) < A):
					findPossibles(a,b,k,(values[0]+math.pow(2,depth),values[1]),depth + 1)
				if(values[1]+math.pow(2,depth) < B):
					findPossibles(a,b,k,(values[0],values[1]+math.pow(2,depth)),depth + 1)
				findPossibles(a,b,k,(values[0],values[1]),depth + 1)
			else:
				if(values[0]+math.pow(2,depth) < A and values[1]+math.pow(2,depth) < B):
					findPossibles(a,b,k,(values[0]+math.pow(2,depth),values[1]+math.pow(2,depth)),depth + 1)

		for j in range(0, K):
			findPossibles(A,B,j, (0,0), 0)

		ct = 0;

		#prt(str(possiblePairs))

		prt(str(len(possiblePairs))+"\n")

		#return

main()