T = int(raw_input())

def is_non_decreasing(n):
	digits = [int(x) for x in str(n)]
	return all(digits[i+1] >= digits[i] for i in range(len(digits)-1))

def get_non_decreasing(n):
	if is_non_decreasing(n):
		return n
	else:
		return 10*get_non_decreasing(n/10-1) + 9

for test_case in range(T):
	N = int(raw_input())
	answer = get_non_decreasing(N)
	print "Case #%s: %s"%(test_case+1,answer)
