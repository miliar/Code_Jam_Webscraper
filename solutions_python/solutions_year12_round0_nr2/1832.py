import sys

f = open("test.in")

num = int(f.readline())

def solve_no_surprise(p,val):
	score = 0
	if (val%3 ==0 ):
		score = val/3
	elif(val%3 ==1):
		score = val/3 + 1
	else :
	 	score = val/3 + 1
	if (val < 3) :
		if (val >= p ) :
			return 1
		else :
			return 0
	if (score >= p) :
		return 1
	else:
		return 0

def solve_surprise(p, val) :
	score = 0
	if (val % 3 == 0) :
		score =  val/3 + 1
	elif (val % 3 == 1) :
		score =  val/3 + 1
	else :
	 	score =  val/3 + 2
	if (val < 3) :
		if (val >= p) :
			return 1
		else:
		 	return 0
	if (score >= p) :
		return 1
	else :
	 	return 0

def solve(solution, surprise, p, i, value):
	sur_val = 0
	max_val = 0
	if (i < len(value)) :
		v = int(value[i])
		if (v%3 == 1 or v > 27) :
			solution[surprise][i] = solve_no_surprise(p,int(value[i])) + solve(solution, surprise, p, i+1, value)
		else :
			if (surprise >= 1):
				sur_val = solve_surprise(p,int(value[i])) + solve(solution, surprise-1, p, i+1, value)
			max_val = solve_no_surprise(p,int(value[i])) + solve(solution, surprise, p, i+1, value)
			solution[surprise][i] = max(max_val, sur_val)
		return solution[surprise][i]
	return 0

for i in range(0, num):
	line = f.readline()
	split = line.split()
	surprise = int(split[1])
	p = int(split[2])
	ent = int(split[0])
	solution = []
	for j in range(0, surprise+1) :
		solution.append([])
		for k in range(0, ent) :
			solution[j].append(0)
	print "Case #" + str(i+1) + ": " + str(solve(solution, surprise, p, 0, split[3:]))

