import sys

data = sys.stdin.readlines()
tests = int(data[0])

def solve(s):
	s = map(lambda x: int(x),s.split())
	result = 0
	for i in range(len(s)):
		if s[i] != i+1:
			result = result + 1
	return result


for i in range(1,tests+1):
	result = solve(data[2*i])
	print "Case #%d: %d"%(i,result)
