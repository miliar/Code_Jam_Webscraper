#!/bin/python

def solveTest():
	# Reading input
	inStr = input()
	split = inStr.split(' ')
	factoryCost = float(split[0])
	factoryProd = float(split[1])
	toProduce = float(split[2])
	
	factoriesTimeCost = 0
	curProd = 2
	prev = 2*toProduce # Fake result, > cur
	cur = toProduce/2 # First real result (no factories built)
	while prev > cur:
		prev = cur
		factoriesTimeCost += (factoryCost / curProd)
		curProd += factoryProd
		cur = factoriesTimeCost + toProduce / curProd
	return prev

nbTests = int(input())
for test in range(1,nbTests+1):
	print("Case #"+str(test)+": "+str(solveTest()))
