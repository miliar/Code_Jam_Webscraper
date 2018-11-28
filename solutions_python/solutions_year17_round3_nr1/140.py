import sys
import math
import itertools

def solve(N, K, cakes):
	best = 0
	bestStack = []
	for stack in itertools.combinations(cakes, K):
		area = max(c[0] for c in stack) ** 2
		for cake in stack:
			area += cake[0] * 2 * cake[1]
		if area > best:
			best = area
			bestStack = stack
	return best * math.pi


def tallest(cakes, lessThanThisRadius, number, skip):
	valid = []
	skipDone = False
	for cake in cakes:
		if cake[0] <= lessThanThisRadius:
			if cake == skip and not skipDone:
				skipDone = True
				continue
			valid.append(cake)
	short = sorted(valid, key=lambda c: c[0] * c[1])
	tall = short[::-1]
	return tall[:number]

def solvebad(N,K,cakes):
	best = 0
	bestStack = []
	for radius in cakes:
		tall = tallest(cakes, radius[0], K-1, radius) + [radius]
		if len(tall) < K:
			continue
		if len(tall) > K:
			1/0
		#area = radius[0] ** 2 * math.pi
		area = max(c[0] for c in tall) ** 2 
		for cake in tall:
			area += cake[0] * 2 * cake[1]
		if area > best:
			best = area
			bestStack = tall
	return best*math.pi
	#return best, bestStack

"""
def solvebad(N,K,cakes):
	best = 0
	bestStack = []
	for limit in cakes:
		short = [c for c in cakes if c[0] <= limit[0]]
		if len(short) < K:
			continue
		short.remove(limit)
		area = limit[0] ** 2 * math.pi
		short = sorted(short, key=lambda cake: cake[0]*cake[1])[::-1][:K-1]
		short.append(limit)
		for cake in short:
			area += cake[0] * 2 * math.pi * cake[1]
		if area > best:
			best = area
			bestStack = short
	return best, bestStack
"""

T = int(input())
for case in range(T):
	N,K = map(int, input().split())
	cakes = [list(map(int, input().split())) for _ in range(N)]
	ans = solvebad(N,K,cakes)
	#cA = solve(N,K,cakes)
	#wA = solvebad(N,K,cakes)
	#if cA != wA:
		#print(cA - wA)
		#print(N,K,cakes, cS, wS)
	#op = "Case #{}: {}".format(case+1, solve(N,K,cakes))
	op = "Case #{}: {}".format(case+1, ans)
	print(op)
	sys.stderr.write(op + "\n")
