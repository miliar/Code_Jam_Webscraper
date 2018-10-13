def solution(S):
	if len(S) == 1:
		return S
		
	index = get_non_tidy_index(S)

	if index == -1:
		return S
		
	delta = int(S[index:]) + 1

	return solution(str(int(S) - delta))

def get_non_tidy_index(S):
	temp = 0
	for i,number in enumerate(S):
		if number >= temp:
			temp = number
			continue
		else:
			return i
	return -1

if __name__ == "__main__":
	test_cases = input()
	for case in xrange(1, test_cases + 1):
		S = raw_input()  
		print "Case #%i: %s" %  (case, solution(S))
