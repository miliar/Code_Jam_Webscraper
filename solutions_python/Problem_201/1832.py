# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(t):
	#if i == 3: 
	#	break
	nb_stalls, nb_people = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	stalls = [ nb_stalls ]
	
	for p in range(nb_people): 
		max_space = max(stalls)
		if max_space % 2 > 0:
			ls = int((max_space - 1) / 2)
			rs = int((max_space - 1) / 2)
		else: 
			ls = int(max_space / 2  - 1)
			rs = int(max_space / 2)
		
		idx = stalls.index(max_space)
		#print("stalls %s - idx %d - ls: %d - rs: %d" % (stalls, idx, ls, rs))
		next_stalls = []
		if idx > 0: 
			next_stalls += stalls[:idx]
		if ls > 0:
			next_stalls.append(ls)
		if rs > 0:
			next_stalls.append(rs)
		if idx < len(stalls): 
			next_stalls += stalls[idx+1:]
		stalls = next_stalls
		#print(stalls)

		y = int(max(ls, rs))
		z = int(min(ls, rs))
	print("Case #{}: {} {}".format(i+1, y, z))

 # X....X
 # X.X..X
 # X.XX.X