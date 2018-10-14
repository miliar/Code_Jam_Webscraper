#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import *

def find_indSecondaire(stall_list):
	listIndDiffZero = []
	listPossibles = []
	for i in range(len(stall_list)):
		if stall_list[i] != 0:
			listIndDiffZero.append(i)
	for i in range(len(listIndDiffZero)-1):
		indSecondaireLeft = listIndDiffZero[i]
		indSecondaireRight = listIndDiffZero[i+1]
		listPossibles.append((indSecondaireLeft, indSecondaireRight))
	return listPossibles

def calcul_dist(indSecondaireLeft, indSecondaireRight):
	#vu que Ls = indPrincipal - indSecondaireLeft - 1
	#et vu que Rs = indSecondaireRight - indPrincipal - 1
	# on cherche à résoudre pour quel indPrincipal Ls = Rs
	distTuple = indSecondaireRight - indSecondaireLeft
	indPrincipal = (indSecondaireRight + indSecondaireLeft) / 2 # toujours positif puisque indSecondaireRight toujours supérieur à indSecondaireLeft
	if type(indPrincipal) == int:
		Ls = indPrincipal - indSecondaireLeft - 1
		Rs = indSecondaireRight - indPrincipal - 1
		#print "Ls", Ls
		#print "Rs", Rs
		return indPrincipal, Ls, Rs, distTuple
	else:
		indPrincipal = floor(indPrincipal)
                Ls = indPrincipal - indSecondaireLeft - 1
                Rs = indSecondaireRight - indPrincipal - 1
                #print "Ls", Ls
                #print "Rs", Rs
		return indPrincipal, Ls, Rs, distTuple

def calcul_bestdistSecondaire(listPossibles):
	listPrincipalPossibles = []
	listSecondairePossibles = []
	listDistTuple = []
	for i in listPossibles:
		indSecondaireLeft, indSecondaireRight = i
		indPrincipal, Ls, Rs, distTuple = calcul_dist(indSecondaireLeft, indSecondaireRight)
		listPrincipalPossibles.append(indPrincipal)
		listSecondairePossibles.append((Ls, Rs))
		listDistTuple.append(distTuple)
	maxDistExistTuple = max(listDistTuple)
	maxIndDistExistTupleList = [i for i, j in enumerate(listDistTuple) if j == maxDistExistTuple]
	#print "maxIndDistExistTupleList", maxIndDistExistTupleList
	indMostLeftTuple = maxIndDistExistTupleList[0]
	tupleKept = listPossibles[indMostLeftTuple] 
	indPrincipalKept = listPrincipalPossibles[indMostLeftTuple]
	distTupleKept = listSecondairePossibles[indMostLeftTuple]
	return tupleKept, indPrincipalKept, distTupleKept
	

def main():

	t = int(raw_input())  # read a line with a single integer

	for i in xrange(1, t + 1):

		N, K = [int(s) for s in raw_input().split(" ")]
		stall_list_origin = [0]*(N+2)
		stall_list_origin[0] = -1 # 1 == first guard
		stall_list_origin[-1] = -1 # 1 == second guard
		stall_list = stall_list_origin
		#print "stall_list ", stall_list
		
		for j in xrange(1, K+1):
			
			listPossibles = find_indSecondaire(stall_list)
			#print "listPossibles", listPossibles
			tupleKept, indPrincipalKept, distTupleKept = calcul_bestdistSecondaire(listPossibles)
			stall_list[indPrincipalKept] = j
		#print "tupleKept", tupleKept
		#print "distTupleKept", distTupleKept
		print "Case #{}: {} {}".format(i, max(distTupleKept), min(distTupleKept))
		#print "stall_list ", stall_list


if __name__ == '__main__':
	main()
