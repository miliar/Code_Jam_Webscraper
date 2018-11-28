#!/usr/bin/python3
from math import floor, ceil
inputFile = "3_small_1.in"

def processTestCase(N, K):
	def occupy(distances):
		mdist = max(distances)
		ndist1, ndist2 = calculateDistance(distances)
		distances.remove(mdist)
		distances.append(ndist1)
		distances.append(ndist2)
	def calculateDistance(distances):
		mdist = max(distances)
		return (ceil((mdist - 1) / 2), floor((mdist - 1) / 2))
	distances = [N]
	for i in range(K - 1):
		occupy(distances)
	return calculateDistance(distances)

with open(inputFile) as f:
	content = f.read().split("\n")[1:-1]
	i = 1
	for line in content:
		N, K = line.split(" ")
		print("Case #%d: %d %d" % ((i, ) + processTestCase(int(N), int(K))))
		i += 1

