# -*- coding: utf8 -*-
from __future__ import division # bien vu!!
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

outFile = open('output_problem_A.txt', 'w')
inFile = open('A-large.in', 'r')
#inFile = open('test.in', 'r')
#inFile = open('final_round.in', 'r')

class Input:
	def __init__(self):
		self.T = None
		self.A = []
		self.N = []
input = None

def solve(S_max, A):
	cpt = 0
	res = 0
	
	for i in range(len(A)):
		if i > cpt + res:
			res = res + (i- (cpt + res))
		cpt += A[i]
	
	return res
	

def main():
	global input
	input = Input()
	# la plupart du temps, les fichier contiennent des listes d'entiers
	# donc la, on met la liste d'entiers du fichier dans N
	
	T = int(inFile.readline())
	print(T)
	
	for t in range(T):
		
		S_max, A = [str(x) for x in inFile.readline().split()]
		S_man = int(S_max)
		A = [int(x) for x in A]
		#print(S_max, A)
	
		res = solve(S_max, A)
		
		print("Case #" + str(t+1) +": " + str(res))
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
    
