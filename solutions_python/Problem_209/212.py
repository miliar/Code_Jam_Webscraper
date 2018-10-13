import math
class pancake:
	def __init__(self, a, b):
		self.r = int(a)
		self.h = int(b)
		self.sidearea = 2 * math.pi * self.r * self.h
		# self.sidearea = 2 * self.r * self.h
		self.uparea = math.pi * self.r ** 2
		# self.uparea = self.r ** 2
	def __str__(self):
		return "{} and {}".format(self.r, self.h)
f = open("A-large.in")
inputdata = []
for l in f:
	inputdata.append(l.strip())
input_p = 1
case = 1
while input_p < len(inputdata):
	n = int(inputdata[input_p].split(' ')[0])
	k = int(inputdata[input_p].split(' ')[1])
	pancake_list = []
	for i in range(n):
		pancake_list.append(pancake(inputdata[input_p + i + 1].split(' ')[0], inputdata[input_p + i + 1].split(' ')[1]))
	pancake_list.sort(key = lambda a: a.r, reverse=True)
	max_area = 0
	# for i in range(len(pancake_list)):
	# 	print(pancake_list[i].r)
	for i in range(len(pancake_list)):
		area = pancake_list[i].uparea + pancake_list[i].sidearea
		# print("first pan: " + str(pancake_list[i]))
		# print("area: " + str(area))
		if i + k > n:
			break
		npanlist = pancake_list[i + 1:]
		npanlist.sort(key = lambda a: a.sidearea, reverse=True)
		for j in range(k - 1):
			area += npanlist[j].sidearea
			# print(str(npanlist[j]))
		if max_area < area:
			max_area = area
		# if i + k > n:
		# 	break
		# for j in range(k):
		# 	area += pancake_list[i + j].sidearea
		# if max_area < area:
		# 	max_area = area
	print("Case #{}: {:.9f}".format(case, max_area))
	case += 1
	input_p += n + 1

