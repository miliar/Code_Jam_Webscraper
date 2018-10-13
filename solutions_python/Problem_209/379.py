import math
import itertools

pi = math.pi

def surface(pancakes):
	previousr = 0.0
	surface = 0.0
	for p in pancakes:
		subsurf = pi*p[0]*p[0]
		subsurf += 2*pi*p[0]*p[1]
		subsurf -= previousr
		surface += subsurf
		previousr = pi*p[0]*p[0]
	return surface

t = int(input())
for test in range(t):
	n,k = [int(a) for a in input().split()]
	pancakes = []
	for p in range(n):
		r,h = [int(a) for a in input().split()]
		pancakes.append([r,h])
	pancakes.sort()
	possibilites = itertools.combinations(pancakes, k)
	result = max([surface(p) for p in possibilites])
	print("Case #{}: {}".format(test+1, result))
