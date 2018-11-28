import sys

T = int(sys.stdin.readline())

for k in xrange(T):
	S,K = sys.stdin.readline()[:-1].split(" ")
	K = int(K)
	S = S.replace("+","1")
	S = S.replace("-","0")
	n = int(S,2)
	a = int ("1" * K, 2)
	found = False
	min = 0
	for i in xrange(2**len(S)):
		ans = n
		p = bin(i)[2:]
		for j,c in enumerate(p[::-1]):
			if c == '1':
				b = a << j
				ans ^= b
		if ans == (2**len(S) - 1):
			found = True
			min = p.count("1") 

	if not found:
		print "Case #{}: {}".format(k+1, "IMPOSSIBLE")
	else:
		print "Case #{}: {}".format(k+1, min)

