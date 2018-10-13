#! /usr/bin/env python3
minimum_time = float("inf")
count = 0
def root(case):
	global count
	global minimum_time
	line = input().split(' ')
	cost = float(line[0])
	increase = float(line[1])
	goal = float(line[2])
	production = float(2)
	count = 0
	minimum_time = float("inf")
	print("Case #{0}: {1:.7f}".format(i, solve(cost, increase, goal, production)))
"""
def solve(c, f, x, p, time, depth):
	global minimum_time
	global count
	#Wait it out
	righttime = time + x/p
	#print("Righttime: {}".format(righttime))
	minimum_time = min(minimum_time, righttime)
	count+=1

	lefttime = time + c/p
	p += f
	if (depth > 900):
		print("going deep, c/p:", str(c/p))
	if (lefttime > minimum_time or lefttime > righttime or c/p < 1e-6):
		print("going nowhere")
		return righttime	
	if (count > 10000):
		print("too deep, production:{0}, c/p:{1}".format(p, c/p))
		return righttime
	lefttime = solve(c, f, x, p, lefttime, depth+1)
	last = lefttime
	#print(lefttime)
	minimum_time = min(minimum_time, lefttime)
	#print("Returning {}".format(min(righttime,lefttime)))
	return min(righttime, lefttime)	
"""
def solve(c, f, x, p):
	time = 0
	last = float("inf")
	while 1:
		righttime = time + x/p
		if (last < righttime): return last
		time += c/p
		p += f
		last = righttime
num_tests = int(input())

for i in range(1,num_tests+1):
	root(i)

