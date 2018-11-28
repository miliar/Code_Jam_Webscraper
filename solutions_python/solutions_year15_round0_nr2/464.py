import sys

def solve(p):
	time = max(p)
	stack_size = 2

	# Assume we want to eat pancakes in stack_size time
	while stack_size < max(p):
		ssum = 0
		for Pi in p:
			# How many moves are required to divide stack of size Pi to stack(s) of stack_size size?
			ssum += (Pi - 1) // stack_size

		time = min(time, ssum + stack_size) # Need to add time for eating remaining biggest stack
		stack_size += 1
		
	return time


f = open(sys.argv[1])
t = int(f.readline())

for _t in range(t):
	d = f.readline()
	p = f.readline().split()
	p = [int(p[i]) for i in range(len(p))]
	
	print("Case #%d: %d" % (_t+1, solve(p)))