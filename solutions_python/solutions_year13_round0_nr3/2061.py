from parser import parse
from itertools import permutations
from math import sqrt

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def helper(test):
	sol = set()
	a,b = test
	lower = max(len(str(int(sqrt(a))))/2,1)
	upper = len(str(int(sqrt(b))))/2+1
	for i in range(lower, upper+1):
		for perm in permutations(nums, i):
			s = ''.join(perm)
			m = int(s + s[::-1])
			n = int(s + s[::-1][1:])
			sq = str(pow(m,2))
			if sq == sq[::-1]:
				sqi = int(sq)
				if a <= sqi <= b:
					sol.add(sqi)
			sq = str(pow(n,2))
			if sq == sq[::-1]:
				sqi = int(sq)
				if a <= sqi <= b:
					sol.add(sqi)
	return len(sol)

schema = [(),[lambda x: map(int, x.split())]]
num_tests,tests = parse(schema)
for case,test in enumerate(tests):
	sol = helper(test)
	print 'Case #{}: {}'.format(case+1, sol)
