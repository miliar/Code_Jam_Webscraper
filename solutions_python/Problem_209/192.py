#coding=utf-8

import math

def calculs(diametre, hauteur):
	surface = math.pi * diametre * diametre
	tranche = 2 * math.pi * diametre * hauteur

	return (surface, tranche)

def traiterCas(pancakes, k):
	maxExpo = 0
	expositions = []
	for (d,h) in pancakes:
		expositions.append(calculs(d, h))
	#On sélectionne le plus grand pancake
	for p in range(0, len(pancakes)):
		maxD, hauteur = pancakes[p]
		surface, tranche1 = expositions[p]
		totalExpo = surface + tranche1

		tranches = []
		for j in range(0, len(pancakes)):
			if j == p:
				continue
			(d, h) = pancakes[j]
			if d > maxD:
				continue
			s, t = expositions[j]
			tranches.append(t)

		if k != 1:
			if len(tranches) < k - 1:
				continue

			tranches.sort(reverse=True)
			for i in range(0, k-1):
				totalExpo = totalExpo + tranches[i]

		if totalExpo > maxExpo:
			maxExpo = totalExpo

	return maxExpo

t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	chaine = raw_input()
	(n, k) = (int(i) for i in chaine.split())
	pancakes = [];
	for l in range(0, n):
		(diametre, hauteur) = (int(j) for j in raw_input().split())
		pancakes.append((diametre, hauteur))
	print "Case #%d: %f" % (i, traiterCas(pancakes, k))