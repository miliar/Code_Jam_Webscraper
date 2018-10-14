def work(z):
	z.sort()
	i = 0
	while i < len(z) - 1:
		if z[i][0] == z[i + 1][0]:
			z[i] = (z[i][0], z[i][1] + z[i + 1][1])
			del z[i + 1]
		else:
			i += 1
	d0 = 0
	dmin = 0
	for t, d in z:
		d0 += d
		dmin = min(dmin, d0)
	return -dmin
			
N = int(raw_input())
for Case in range(0, N):
	T = int(raw_input())
	na, nb = raw_input().strip().split()
	NA = int(na)
	NB = int(nb)
	tA = []
	tB = []
	for i in range(0, NA):
		A, B = raw_input().strip().split()
		a = int(A[0:2]) * 60 + int(A[3:5])
		b = int(B[0:2]) * 60 + int(B[3:5])
		tA.append((a, -1))
		tB.append((b + T, +1))
	for i in range(0, NB):
		B, A = raw_input().strip().split()
		b = int(B[0:2]) * 60 + int(B[3:5])
		a = int(A[0:2]) * 60 + int(A[3:5])
		tB.append((b, -1))
		tA.append((a + T, +1))
	print "Case #" + str(Case + 1) + ":", work(tA), work(tB)
