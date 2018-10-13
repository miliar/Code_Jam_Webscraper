import math

file = open("C-small-1-attempt0.in", "r")
contains = file.read().split("\n")
lines = int(contains[0])
cases = contains[1 : lines+1]

output = open("C-small-1-attempt0.out", "w")

cnt = 0
for i in cases:
	cnt += 1
	case = i.split()
	n = int(case[0])
	k = int(case[1])
	stalls = [n]
	for j in range(0,k):
		choose = max(stalls)
		maximal = math.ceil((choose - 1) / 2)
		minimal = math.floor((choose - 1) / 2)
		stalls.append(maximal)
		stalls.append(minimal)
		stalls.remove(choose)	
	output.write("Case #" + str(cnt) + ": " + str(maximal) + " " + str(minimal) + "\n")
	

	



