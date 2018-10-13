map = {0:0, 1:1, 2:3, 3:6, 4:10, 5:15, 6:21, 7:28, 8:36, 9:45, 10:55, 11:66, 12:78, 13:91, 14:105}

def num_combos(num, lower, upper, seen):
	n = 0
	if num in seen: return 0
	seen[num] = True
	for i in xrange(0, len(num)):
		new = num[i:] + num[:i]
		if new not in seen:
			seen[new] = True
			newnum = int(new)
			if newnum >= lower and newnum <= upper: 
				n += 1
	return n
	
	
def find_solution(lower, upper):
	seen = {}
	num = 0
	for i in xrange(lower, upper + 1):
		temp = map[num_combos(str(i), lower, upper, seen)]
		num += temp
	return num
	
fin = open("C-large.in.txt", "r")
fout = open("output.txt", "w")

inputs = fin.read().split("\n")[1:]
i = 1
for inp in inputs:
	ip = inp.split()
	answer = find_solution(int(ip[0]), int(ip[1]))
	print "Case #" + str(i) + ": " + str(answer)
	fout.write("Case #" + str(i) + ": " + str(answer) + "\n")
	i += 1