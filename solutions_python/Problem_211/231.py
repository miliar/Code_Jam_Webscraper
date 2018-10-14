number = raw_input()

def parseInput(example, fl=False):
	stripped_example = example.strip()
	if fl:
		return map(float, stripped_example.split(" "))
	else:
		return map(int, stripped_example.split(" "))

def calculateProbability(N, K, cores):
	if K > N:
		return 0
	if K == 1:
		p = 1
		for i in range(N):
			p *= 1 - cores[i]
		return 1 - p
	if K == N:
		p = 1
		for i in range(N):
			p *= cores[i]
		return p
	return cores[0]*calculateProbability(N-1, K-1, cores[1:]) + (1- cores[0])*calculateProbability(N-1, K, cores[1:])

def solve(N, K, U, cores):
	crs = sorted(cores)[::-1] 	
	lst = crs[:K][::-1]
	lst.append(1)
	for i in range(K):
		needed = (i+1)*(lst[i + 1] - lst[i])
		using = min(needed, U)
		U -= using
		added_per_core = using/float(i + 1)
		for j in range(i + 1):
			lst[j] += added_per_core
		if U == 0:
			break
	del lst[-1]
	leftover = crs[K:][::-1]
	leftover.append(1)
	if U > 0:
		
		for i in range(len(leftover) - 1):
			needed = (i+1)*(leftover[i + 1] - leftover[i])
			using = min(needed, U)
			U -= using
			added_per_core = using/float(i + 1)
			for j in range(i + 1):
				leftover[j] += added_per_core
			if U == 0:
				break
	del leftover[-1]
	crs = lst + leftover
	return calculateProbability(N, K, crs)

for n in xrange(int(number)):
	example = raw_input()
	(N, K) = parseInput(example)
	[U] = parseInput(raw_input(), True)
	cores = parseInput(raw_input(), True)
	print "Case #" + str(n + 1) +": " + str(solve(N,K,U,cores))