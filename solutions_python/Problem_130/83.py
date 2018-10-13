T = input()

def b0(n):
	q = bin(P-1)[2:]
	if '0' not in q:
		return 0
	return 1

def l0(l,n):
	q = int('1'*l+'0'*(n-l), 2)
	return q + 1

for cs in range(1, T+1):
	[N, P] = map(int, raw_input().strip().split())
	ppl = pow(2, N)

	# generate lex string for prize w/ least # of wins
	q = bin(P-1)[2:]
	min_w = b0(P) + (N-len(q))
	q = '0' * (N-len(q)) + q
	# print len(bin(P-1)[2:])	
	# print q, min_w, b0(P)
	bp = pow(2, min_w)

	x = 0
	while l0(x,N) <= P:
		x += 1
	# print l0(1,3)
	# print pow(2, x) - 2
	# print l0(3,N)

	print "Case #%d: %d %d" % (cs, min(ppl-1, pow(2, x) - 2), ppl-bp)