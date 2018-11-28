import sys

def solve(N,K,U,P):
	P = sorted(P) + [1]
	for i in range(len(P)-1):
		imp = P[i+1] - P[i]
		if imp * (i+1) <= U:
			gain = imp
		else:
			gain = U / float(i+1)
		for j in range(i+1):
			P[j] += gain
			U -= gain
		if U < -0.0000000001:
			print(U)
			1/0
	prod = 1
	for n in P:
		prod *= n
	if prod < .00000001:
		prod = 0
	return prod

T = int(input())
for case in range(T):
	N,K = map(int, input().split())
	U = float(input())
	P = map(float, input().split())
	op = "Case #{}: {}".format(case+1, solve(N,K,U,P))
	print(op)
	sys.stderr.write(op + "\n")
