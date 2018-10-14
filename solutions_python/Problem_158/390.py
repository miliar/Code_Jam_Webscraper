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

outFile = open('output_problem_D.txt', 'w')
inFile = open('D-small-attempt1.in', 'r')
#inFile = open('test.in', 'r')
#inFile = open('final_round.in', 'r')

class Input:
	def __init__(self):
		self.T = None
		self.A = []
		self.N = []
input = None
	
def solve(X, R, C):
	if(X == 1) or (X == 2 and (R*C)%2 == 0):
		return "GABRIEL"
	elif (X==2 and (R*C)%2 == 1):
		return "RICHARD"
	elif min(R,C) == 1:
		return "RICHARD"
		
	cas1 = R==4 and C==4
	cas2 = R==3 and C ==3
	cas3 = R==2 and C == 2
	
	cas4 = (R==4 and C == 3) or (R==3 and C == 4) 
	cas5 = (R==4 and C == 2) or (R==2 and C == 4)
	cas6 = (R==3 and C == 2) or (R==2 and C == 3)

	if cas1:
		if X == 4:
			return "GABRIEL"
		elif X == 3:
			return "RICHARD"
	elif cas2:
		if X==4:
			return "RICHARD"
		elif X==3:
			return "GABRIEL"
	elif cas3:
		if X==4 or X == 3:
			return "RICHARD"
	elif cas4:
		if X==4 or X==3:
			return "GABRIEL"
	elif cas5:
		if X==4 or X==3:
			return "RICHARD"
	elif cas6:
		if X==4:
			return "RICHARD"
		elif X==3:
			return "GABRIEL"
	else:
		return "GROS PBBB !!!!!!!!!"
def main():
	global input
	input = Input()
	# la plupart du temps, les fichier contiennent des listes d'entiers
	# donc la, on met la liste d'entiers du fichier dans N
	
	T = int(inFile.readline())
	print(T)
	
	for t in range(T):
		
		X, R, C = [int(x) for x in inFile.readline().split()]
		
		#print(X, R, C)
		res = solve(X, R, C)
		
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
    
