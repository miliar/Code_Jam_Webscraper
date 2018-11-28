import sys
def read_input():
	'''
	Returns a list of test_cases, each of which has:
		[N, S, p, [result1, result2, ...]]
	'''	
	data = sys.stdin.readlines()
	#print data
	test_cases = []
	for test_case in data[1:]:
		line_splitted = test_case.split()
		test_cases.append([int(line_splitted[0]), int(line_splitted[1]), int(line_splitted[2]), map(lambda x: int(x), line_splitted[3:])])
	return test_cases

def find_max_p_score(S, p, results):
	'''
	Finds max p score that have been received by googlers.
	
	S - surprising scores
	p - score value to be found
	results - consecutive scores
	'''
	#print 'S, p, results:', S, p, results
	
	need_s = 0
	dont_need_s = 0
	#for each googler check, wether he needs surprising score to achieve p or not:
	for result in results:
		#print 'considering result:', result
		#check score with no surprise:
		best_score_no_surprise = 0
		for k in reversed(range(1, 21)):
			if k + 2*(k-1) == result or 2*k + k-1 == result:
				best_score_no_surprise = k
				break
		if result % 3 == 0:
			best_score_no_surprise = max(best_score_no_surprise, result/3)
		#print 'best_score_no_surprise:', best_score_no_surprise
		
		if best_score_no_surprise >= p:
			dont_need_s += 1
		else:
			#check if surprise helps:
			best_score_surprise = 0
			for k in reversed(range(2, 21)):
				if k + (k-1) + (k-2) == result or 2*k + k-2 == result or k + 2*(k-2) == result:
					best_score_surprise = k
					break
			if best_score_surprise >= p:
				need_s += 1
				
			#print 'best_score_surprise:', best_score_surprise
	
		#print 'need_s:', need_s
		#print 'dont_need_s:', dont_need_s

	return dont_need_s + min(need_s, S)

test_cases = read_input()
#print "test_cases:", test_cases

for ind, test_case in enumerate(test_cases):
	max_p_scores = find_max_p_score(test_case[1], test_case[2], test_case[3])
	print "Case #"+str(ind+1)+": "+str(max_p_scores)
