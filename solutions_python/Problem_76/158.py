T = int(raw_input())

def pcalc(a,b):
	sum = 0
	for i in range(22):
		bitA = (a >> i) & 1
		bitB = (b >> i) & 1
		if bitA and bitB :
			bitR = 0
		elif bitA | bitB:
			sum += 1 << i
	return sum

def solveCase(elements):
	l1 = []
	
	l2 = elements[:]
	l2.sort()
	l2.reverse()
	
	weightL1 = 0
	
	weightL2 = 0
	for e in candies:
		weightL2 = pcalc(weightL2,e)
	
	#print "L : %s  weights( %d, %d )" % (l2, weightL1, weightL2)
	passed = False
	while weightL1 != weightL2 or not passed:
		if not l2:
			return -1
		outE = l2.pop()
		weightL1 = pcalc(weightL1,outE)
		weightL2 = pcalc(weightL2,outE)
		#print "L : %s  weights( %d, %d )" % (l2, weightL1, weightL2)
		if not passed:
			passed = True
	return sum(l2)
	
for t in range(1,T+1):
	N = int(raw_input())
	candies = map(int,raw_input().split())
	sol = solveCase(candies)
	
	if sol == -1:
		print "Case #%d: NO" % (t)
	else:
		print "Case #%d: %d" % (t,sol)
		
	