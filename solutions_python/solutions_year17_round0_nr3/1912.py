#GCJ 2017
#Bathroom Stalls

INFILE = "C-small-1-attempt2.in"
OUTFILE = "C-small-1-attempt2.out"

def stalls(K, N):
	stalls = []
	stalls.append(1)
	for i in range(K):
		stalls.append(0)
	stalls.append(1)
	for user in range(N):
		#print(stalls)
		a = choose_stall(stalls)
		if user == N-1:
			return max_dist(stalls, a), min_dist(stalls, a)

def choose_stall(stalls):
	min_stalls = []
	max_stall = 0
	min_val = 0
	max_val = 0
	for i, stall in enumerate(stalls):
		if stall == 0:
			a = min_dist(stalls, i)
			if a > min_val:
				min_val = a
				min_stalls = [i,]
			elif a == min_val:
				min_stalls.append(i)
	#print("minstalls", min_stalls)
	first = True
	for j, stall in enumerate(min_stalls):
		if stalls[stall] == 0:
			a = max_dist(stalls, stall)
			if first:
				max_val = a
				max_stall = stall
				first = False
			if a > max_val:
				max_val = a
				max_stall = stall
	stalls[max_stall] = 1
	return max_stall

def max_dist(stalls, index):
	max = 0
	found = False
	i = 1
	while not found:
		if stalls[index - i] == 1:
			found = True
			max = i
		i += 1
	found = False
	i = 1
	while not found:
		if index + i > len(stalls):
			raise(Exception)
		if stalls[index + i] == 1:
			found = True
			if max < i:
				max = i
		i += 1
	return max - 1

def min_dist(stalls, index):
	min = 0
	found = False
	i = 1
	while not found:
		if stalls[index - i] == 1:
			found = True
			min = i
		i += 1
	found = False
	i = 1
	while not found:
		if stalls[index + i] == 1:
			found = True
			if min > i:
				min = i
		i += 1
	return min - 1

fin = open(INFILE, "r")
fout = open(OUTFILE, "w")

num = fin.readline()
for case in range(int(num)):
	a = fin.readline()
	K, N = a.split()
	out = stalls(int(K), int(N))
	fout.write("Case #" + str(case + 1) + ": ")
	fout.write(str(out[0]) + " " + str(out[1]) + "\n")
	print(out)
	
fin.close()
fout.close()

