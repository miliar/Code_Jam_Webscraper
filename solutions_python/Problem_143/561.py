with open("input.in", 'r') as infile:
	cases = int(infile.readline())
	results = [0] * cases
	
	for case in range(cases):
		params = infile.readline().split()
		A = int(params[0])
		B = int(params[1])
		K = int(params[2])
		wins = 0
		for a in range(A):
			for b in range(B):
				wins += 1 if (a & b) < K else 0
				
		results[case] = wins
		
	# print out case results
	for case in range(cases):
		print("Case #{}: {}".format(case + 1, results[case]))	