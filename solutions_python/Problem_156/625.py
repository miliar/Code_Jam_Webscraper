import math

def cost_max_pancake(x, l):
	s = sum((math.ceil(float(n)/float(x)) - 1) for n in l if n > x)
	return x + s

def solution(l):
	return min(cost_max_pancake(x,l) for x in range(1,max(l) + 1))

def solve_file(file_name):
	f = open(file_name, "r")
	wf = open("output.txt","w")
	ntestCases = int(f.readline())
	for i in range(1, ntestCases+1):
		if i > 1:
			wf.write("\n")
		nDiners = int(f.readline())
		dinerStr = f.readline()
		global diners
		diners = [int(d) for d in dinerStr.split()]
		wf.write("Case #" + str(i) + ": " + str(int(solution(diners))))


