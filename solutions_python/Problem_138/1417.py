from __future__ import division

import sys
import math
import heapq
import copy

sys.setrecursionlimit(100000) 
T = int(sys.stdin.readline())

def main():
	for case in range(1,T+1):
		res = solve(case)
		sys.stdout.write("Case #{}: {}\n".format(case, res));

def solve(case):
	numberBlocks = int(sys.stdin.readline())
	NaomiBlocks = map(float, sys.stdin.readline().split())
	KenBlocks = map(float, sys.stdin.readline().split())

	resWar = war(numberBlocks, copy.deepcopy(NaomiBlocks), copy.deepcopy(KenBlocks))
	resDWar = dwar(numberBlocks, copy.deepcopy(NaomiBlocks), copy.deepcopy(KenBlocks))

	res = str(resDWar) + " " + str(resWar);
	return res

def war(numberBlocks, NaomiBlocks, KenBlocks):
	naomiePoints = 0
	kenPoints = 0

	for i in range(0, numberBlocks):
		naomiChosen = NaomiBlocks[0]
		kenChosen = chooseKen(naomiChosen, KenBlocks)

		if naomiChosen > kenChosen:
			naomiePoints += 1
		else :
			kenPoints +=1 

		NaomiBlocks.remove(naomiChosen)
		KenBlocks.remove(kenChosen)

	return naomiePoints

def dwar(numberBlocks, NaomiBlocks, KenBlocks):
	naomiePoints = 0
	kenPoints = 0

	for i in range(0, numberBlocks):
		c = chooseNaomie(NaomiBlocks, KenBlocks)
		naomiChosen = c[0]
		naomieTold = c[1]

		kenChosen = chooseKen(naomieTold, KenBlocks)

		if naomiChosen > kenChosen:
			naomiePoints += 1
		else :
			kenPoints +=1 

		NaomiBlocks.remove(naomiChosen)
		KenBlocks.remove(kenChosen)

	return naomiePoints


def chooseNaomie(NaomiBlocks, KenBlocks):
	if len(NaomiBlocks)==1 or min(NaomiBlocks) > max(KenBlocks):
		return [NaomiBlocks[0],NaomiBlocks[0]]
	elif min(NaomiBlocks) < min(KenBlocks):
		chosen = min(NaomiBlocks)
		res = heapq.nlargest(2, KenBlocks)
		told = float(res[0] + res[1]) / 2 
		return [chosen,told]
	else:
		chosen = min(NaomiBlocks)
		told = float(max(KenBlocks)+1)/2
		return [chosen,told]


def chooseKen(naomiChosen, KenBlocks):
	largerBlocks = []
	for b in KenBlocks:
		if b > naomiChosen:
			largerBlocks.append(b)

	if len(largerBlocks):
		return min(largerBlocks)

	else :
		return min(KenBlocks)

main()