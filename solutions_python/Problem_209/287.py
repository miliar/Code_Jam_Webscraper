import sys
import math

def pancake_value(top, side, max_top):
	if top > max_top:
		return top - max_top + side
	else:
		return side

for i in range(0, int(sys.stdin.readline())):
	inputs = sys.stdin.readline()[:-1].split(" ")
	n = int(inputs[0])
	k = int(inputs[1])
	
	pancakes = []
	r = []
	h = []
	for j in range(0, n):
		inputs = sys.stdin.readline()[:-1].split(" ")
		r.append(int(inputs[0]))
		h.append(int(inputs[1]))
		pancakes.append( (r[j], h[j]) )
	
	pancakes.sort(reverse=True)
	
	sa_side = []
	sa_top = []
	for p in pancakes:
		sa_side.append(2 * math.pi * p[0] * p[1])
		sa_top.append(math.pi * p[0] ** 2)
	
	sa = 0
	used = []
	max_top_used = 0
	while len(used) < k:
		best_value = -1
		for j in range(0, n):
			if j in used:
				continue
			if best_value == -1:
				best_value = j
				continue
			if pancake_value(sa_top[j], sa_side[j], max_top_used) > pancake_value(sa_top[best_value], sa_side[best_value], max_top_used):
				best_value = j
		sa += pancake_value(sa_top[best_value], sa_side[best_value], max_top_used)
		if sa_top[best_value] > max_top_used:
			max_top_used = sa_top[best_value]
		used.append(best_value)
	print("Case #" + str(i + 1) + ": " + "{0:.15f}".format(sa))
