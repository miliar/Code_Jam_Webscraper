def solve(s):
	clapping = 0
	added = 0
	for (i,j) in enumerate(s):
		if clapping < i:
			added += i - clapping
			clapping = i
		clapping += int(j)
				
	return added

lines = open("in2.in").readlines()
T = int(lines[0].strip())

for i in range(T):
	s = lines[i+1].split(' ')[1].strip()
	print "Case #%d: %d"%(i+1, solve(s))
