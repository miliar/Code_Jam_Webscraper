import math
testcase_count = int(input())

def additional_surface(r, h, old_max_r):
	if r <= old_max_r:
		return math.pi * 2 * r * h
	else:
		return math.pi * (r * r - old_max_r * old_max_r + 2 * r * h)

for testcase_index in range(testcase_count):
	n, k = map(int, input().split())
	pancakes = []
	for i in range(n):
		pancakes.append(list(map(int, input().split())))
	
	r = 0
	surface = 0
	for i in range(k):
		pancakes.sort(key=lambda pancake: additional_surface(pancake[0], pancake[1], r))
		pancake = pancakes.pop()
		surface += additional_surface(pancake[0], pancake[1], r)
		r = max(r, pancake[0])
	

	print("Case #%d: %f" % (testcase_index + 1, surface))

