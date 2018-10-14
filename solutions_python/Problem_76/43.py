import sys

data = sys.stdin.readlines()
tests = int(data[0])

def solve(s):
	s = map(lambda x: int(x),s.split())
	xor = 0
	min_val = 10**7
	sum_val = 0
	for i in s:
		min_val = min(min_val,i)
		sum_val = sum_val + i
		xor = xor ^ i
	if xor == 0:
		return sum_val - min_val
	else:
		return None	


for i in range(1,tests+1):
	result = solve(data[2*i])
	if result == None:
		print "Case #%d: NO"%(i)
	else:
		print "Case #%d: %d"%(i,result)
