from math import pi
import sys
sys.setrecursionlimit(1200)

class Pancake:
	def __init__(self, radius, height):
		self.radius = radius
		self.height = height

def ampleSyrup(K, pancakes):
	pancakes.sort(key=lambda pancake: pancake.radius, reverse=True)
	return "{0:.6f}".format(maxArea(pancakes, 0, K, K, {}))

def maxArea(pancakes, index, need, K, memory):
	if index == len(pancakes) and need > 0:
		return None
	if need == 0:
		return 0

	if (index, need) not in memory:
		yes = maxArea(pancakes, index + 1, need - 1, K, memory)
		if yes or yes == 0:
			yes += 2 * pi * pancakes[index].radius * pancakes[index].height
			if need == K:
				yes += pi * pancakes[index].radius ** 2
		no = maxArea(pancakes, index + 1, need, K, memory)

		if yes and no:
			memory[(index, need)] = max(yes, no)
		elif yes:
			memory[(index, need)] = yes
		elif no:
			memory[(index, need)] = no
		else:
			memory[(index, need)] = None

	return memory[(index, need)]

T = int(input())
for i in range(T):
	N, K = [int(p) for p in input().split()]
	pancakes = []
	for j in range(N):
		r, h = [int(p) for p in input().split()]
		pancakes.append(Pancake(r, h))
	print('Case #{}: {}'.format(i + 1, ampleSyrup(K, pancakes)))