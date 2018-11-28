import math
t = int(raw_input())

class Pancake:
	def __init__(self, r, h):
		self.r = r
		self.h = h
		self.sideArea = r * h * math.pi * 2

answers = []
for test in range(0, t):
	in_str_split = raw_input().split(' ')
	n = int(in_str_split[0])
	k = int(in_str_split[1])
	pancakes = []
	for i in range(0, n):
		in_str_split = raw_input().split(' ')
		pancakes.append(Pancake(float(in_str_split[0]), float(in_str_split[1])))

	pancakes.sort(lambda x,y: cmp(x, y), lambda x: x.r, True)
	best = 0
	for i in range(0 , n-k + 1):
		radius = pancakes[i].r
		smaller = []
		for j in range(i+1, n):
			smaller.append(pancakes[j])

		smaller.sort(lambda x,y: cmp(x, y), lambda x: x.sideArea, True)
		smaller = smaller[:k-1]

		area = math.pi * radius * radius + pancakes[i].sideArea
		for pan in smaller:
			area += pan.sideArea
		best = max(area, best)

	answers.append(best)


for test in range(0, t):
	out_str = "Case #" + str(test+1) + ": " + str(answers[test]).replace("+", "")
	print out_str