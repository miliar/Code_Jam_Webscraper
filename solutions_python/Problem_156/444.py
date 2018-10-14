# -*- coding: utf8 -*-
from __future__ import division
import sys
import time
import operator
import math
import re
from fractions import Fraction
from multiprocessing import Pool
from itertools import *

#import networkx as nx
from random import randint

printDebug = True #pour activer le debug dans la ligne de command faites : "python hello.py -d"

outFile = open('output_problem_B.txt', 'w')
inFile = open('B-large.in', 'r')
#inFile = open('test.in', 'r')
#inFile = open('final_round.in', 'r')

class Input:
	def __init__(self):
		self.T = None
		self.A = []
		self.N = []
input = None

def solve2(P):
	P.sort(reverse=True)
	cpt = 0
	res = P[0]
	
	while P[0] >= 3:
		P.append(P[0]//2)
		P[0] = P[0]//2 + P[0]%2		
		P.sort(reverse=True)
		cpt += 1
		res = min(res, cpt + P[0])
	
	return res

def solve(P):
	R = list(P)
	R.sort(reverse=True)
	if R[0] <= 3:
		return R[0]
	
	Q = [x-1 for x in R if (x-1) > 0]
	
	R.append(R[0]//2)
	R[0] = R[0]//2 + R[0]%2
	
	return 1 + min(solve(R), solve(Q))
	
def solve3(P):
	m = max(P)
	res = m
	for n in range(1, m + 1):
		cpt = 0
		for i in range(len(P)):
			if P[i] <= n:
				continue
			else:
				tmp = P[i]//n
				if P[i] - tmp*n > 0:
					cpt += tmp
				else:
					cpt += tmp - 1
		res = min(res, n + cpt)
	
	return res
	
def main():
	global input
	input = Input()
	# la plupart du temps, les fichier contiennent des listes d'entiers
	# donc la, on met la liste d'entiers du fichier dans N
	
	T = int(inFile.readline())
	print(T)
	
	for t in range(T):
		
		D = int(inFile.readline())
		P = [int(x) for x in inFile.readline().split()]
				
		#print(P)
		res = solve3(list(P))
		
		#print("Case #" + str(t+1) +": " + str(res))
		outFile.write("Case #" + str(t+1) +": " + str(res) + "\n")
		
def worker(o):
    return o**3


def startPool(tab):
    p = Pool(8)
    return p.map(worker, tab)


#-------------------------------------------------

def debug(m, endLine='\n'):
    if printDebug:
        sys.stdout.write(m)
        sys.stdout.write(endLine)

if __name__ == '__main__':
    startTime = time.clock()
    ret = main()
    sys.stdout.flush()
    sys.stderr.write("Completed in {} seconds.\n".format(time.clock() - startTime))
    outFile.close()
    
