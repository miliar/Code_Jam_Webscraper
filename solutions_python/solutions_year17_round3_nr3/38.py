cases = int(input())

for casenum in range(1,cases+1):
	N, K = ( int(x) for x in input().split() )
	U = float(input())
	P = [float(x) for x in input().split()]

	P.sort()
	while U > 0:
		if P[0] == P[-1]:
			P = [P[0] + U/N] * N
			U = 0
		else:
			i = 1
			while P[i] == P[0]:
				i += 1
			diff = P[i] - P[0]
			amount = min(diff*i, U)
			P[:i] = [P[0] + amount/i]*i
			U -= amount
			P.sort()

	res = 1
	for Pi in P:
		res *= Pi

	print("Case #", casenum, ": ", res, sep="")

