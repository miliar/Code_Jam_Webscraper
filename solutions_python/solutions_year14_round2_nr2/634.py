def solve():
	A, B, K = map(int, raw_input().split(" "))

	count = 0
	for a in xrange(A):
		for b in xrange(B):
			if a & b < K:
				count += 1
	return count


T = int(raw_input())
for t in xrange(1, T + 1):
	print ("Case #%d: " % t ) + str(solve())