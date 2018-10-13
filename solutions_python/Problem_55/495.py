#!/usr/bin/python

def sum(coaster):
	s = 0
	for n in coaster:
		s += n
	return s

def solveCase(index, rides, capacity, groups):
	money = 0
	queue = []
	coaster = []
	for g in groups:
		queue.append(g)
	
	for i in range(rides):
		while len(queue) > 0:
			g = queue[0]
			if g + sum(coaster) > capacity:
				break
			else:
				coaster.append(g)
				money += g
				queue = queue[1:]
		for g in coaster:
			queue.append(g)
		coaster = []
	
	return "Case #%i: %i" % (index, money)

input = open("/Users/george/Downloads/C-small-attempt0.in", "rU").read()

input = input.split("\n")

i = 0
c = 0
output = ""
for i in range(1, len(input), 2):
	if input[i] == "":
		continue
	c += 1
	line1 = input[i].split(" ")
	line2 = input[i + 1].split(" ")
	rides = int(line1[0])
	capacity = int(line1[1])
	groups = []
	for g in line2:
		groups.append(int(g))
	output += solveCase(c, rides, capacity, groups) + "\n"

print output
o = open("/Users/george/Desktop/C-small-attempt0.out", "w")
o.write(output)
o.close()