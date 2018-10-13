import itertools

def solution(N,K):
	if N==K:
		return "0 0"
	
	stalls = "0"*N
		
	for i in range(K):
		(index, minLsRs, maxLsRs) = get_index_to_stall(N, stalls)
		old_stalls = stalls
		bla = 0
		for j,item in enumerate(old_stalls):
			if item == "1":
				continue
			if bla == index:
				temp = list(stalls)
				temp[j] = "1"	
				stalls="".join(temp)
			bla += 1
		#print stalls	

	return "%d %d" % (maxLsRs, minLsRs)

def get_index_to_stall(N, stalls):
	groups = stalls.split("1")
	
	Ls = map(lambda x: range(len(x)), groups)
	#print Ls
	Rs = map(lambda x: x[::-1], Ls)
	#print Rs
	
	temp = map(lambda x: zip(x[0],x[1]), zip(Ls,Rs))
	LsRs = list(itertools.chain(*temp))
	#print ">",LsRs
	
	minLsRs = map(min, LsRs)
	#print ">>",minLsRs
	
	maxLsRs = map(max, LsRs)
	#print ">>",maxLsRs
	
	maxVal = max(minLsRs)
	#print maxVal

	indices = [i for i,x in enumerate(minLsRs) if x == maxVal]
	#print "ind>",indices
	
	index = 0
	
	if len(indices) == 1:
		index = indices[0]
	else:
		tt =map(lambda x: LsRs[x], indices)
		newMaxLsRs = map(max, tt)
		pre_index = newMaxLsRs.index(max(newMaxLsRs))
		index = LsRs.index(tt[pre_index])

	#print index

	minLs = min(LsRs[index])
	#print minLs
	maxRs = max(LsRs[index])
	
	return [index, minLs, maxRs]

if __name__ == "__main__":
	test_cases = input()
	for case in xrange(1, test_cases + 1):
		(N,K) = map(int, raw_input().split(" "))  
		print "Case #%i: %s" %  (case, solution(N,K))
