import sys

T = int(input())

for t in range(T):
	N, K = [int(i) for i in input().split()]
	U = float(input())
	P = [float(i) for i in input().split()]

	while U > 0.0000000001:
		print(U, file=sys.stderr)
		m = 1
		m2 = 1
		nb = 0
		for p in P:
			if p < m:
				m2 = m
				m = p
				nb = 1
			elif p == m:
				nb += 1
			elif p < m2:
				m2 = p
		diff = -1
		if nb * (m2 - m) <= U:
			U -= nb * (m2 - m)
			diff = m2 - m
		else:
			diff = U/nb
			U = 0
		for ip in range(len(P)):
			if P[ip] == m:
				P[ip] += diff

	prob = 1
	for p in P:
		prob *= p
	print("Case #{}: ".format(t+1)+str(prob))