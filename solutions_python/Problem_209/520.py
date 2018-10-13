#anilkumarravuru

p = 3.14159265358979323846264338327950288419716939937510582097494459230
def comp(a,b):
	return a[0]*a[1] - b[0]*b[1]
T = int(raw_input())
for t in range(T):
	N, K = map(int,raw_input().split())
	R = []
	for n in range(N):
		R += [map(int,raw_input().split())]
	R.sort(reverse = True)
	# print R
	maximum = 0
	for j in range(N-K+1):
		# print R
		A = p*R[j][0]*R[j][0] + 2*p*R[j][0]*R[j][1]
		S = sorted(R[j+1:], lambda x,y:-comp(x,y))
		# print S
		for i in range(K-1):
			A += 2*p*S[i][0]*S[i][1]
		if A > maximum:
			maximum = A
			# print maximum
	print("Case #{}: {}".format(t+1, maximum))






