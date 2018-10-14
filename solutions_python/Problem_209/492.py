import math
import copy

t = int(raw_input()) # this is the number of test cases
for i in xrange(1, t+1):
	n, k = str(raw_input()).split()
	n = int(n)
	k = int(k)
	pancakes = []
	for idx in range(n):
		r, h = str(raw_input()).split()
		r = int(r)
		h = int(h)
		pancakes.append([r, r*r+2*r*h, 2*r*h])

	pancakes.sort(key=lambda x: x[0], reverse=True)
	max_area = 0
	# choose best base
	base_pancakes = pancakes[:n-k+1]
	for idx in range(len(base_pancakes)):
		area = base_pancakes[idx][1]
		new_pancake_lst = copy.copy(pancakes)
		new_pancake_lst.pop(idx)
		new_pancake_lst = new_pancake_lst[idx:]
		new_pancake_lst.sort(key=lambda x:x[2], reverse=True)
		for idy in range(k-1):
			area += new_pancake_lst[idy][2]
		if area > max_area:
			max_area = area

	result = '{:.9f}'.format(max_area * math.pi)

	print  "Case #{0}: {1}".format(i, result)