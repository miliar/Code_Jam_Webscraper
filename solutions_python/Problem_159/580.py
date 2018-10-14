import math

def solve(M):
	p = M[0]
	result = [0, 0]
	r = 0
	for c in M[1:]:
		if c < p and r < (p-c):
			r = (p-c)
		p = c
	p = M[0]
	for c in M[1:]:
		if c < p:
			result[0] = result[0] + p - c
		if p < r:
			result[1] = result[1] + p
		else:
			result[1] = result[1] + r
		p = c
	return result

if __name__ == "__main__":
	for i in xrange(1, int(raw_input())+1):
		N = int(raw_input())
		M = map(int, raw_input().split(' '))
		first, second = solve(M)
		print "Case #{}: {} {}".format(i, first, second)

