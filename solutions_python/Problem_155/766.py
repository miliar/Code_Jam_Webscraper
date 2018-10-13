def solution(l):
	cost = 0
	people = l[0]
	for i in range(1,len(l)):
		if people < i:
			cost += i - people
			people += i - people
		people += l[i]
	return cost

def solve_file(file_name):
	f = open(file_name,"r")
	w = open("out.txt", "w")
	ntestcases = int(f.readline())
	for i in range(1, ntestcases+1):
		if i > 1:
			w.write("\n")
		s = f.readline()
		temp = s.split()
		global maxShyness 
		maxShyness = int(temp[0])
		global people
		people = [int(s2) for s2 in temp[1]]
		w.write("Case #" + str(i) + ": " + str(solution(people)))
