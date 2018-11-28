def isTidyNumber(N):
	#if single digit
	if N < 10:
		return N
	number = str(N)
	for index, item in enumerate(number):
		#print index, item
		if index != 0:
			if item < number[index-1]:
				return False
	return True


def solve(N):
        while not isTidyNumber(N):
        	N-=1
        return N


#B.py - Tidy Numbers
T = input()
for i in range(1, T+1):
	N = input()
	ans = "Case #" + str(i) + ": " + str(solve(N))
	print ans
