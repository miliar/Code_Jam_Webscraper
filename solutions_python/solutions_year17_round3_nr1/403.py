import gcj, math

#gcj.set_sample()

ifile, ofile = gcj.get_files('A')

T = int(ifile.readline().strip())
for t in range(T):
	#sorted(range(len(s)), key=lambda k: s[k])
	(N, K) = list(map(int, ifile.readline().split()))
	R, H = [], []
	for n in range(N):
		(r, h) = list(map(int, ifile.readline().split()))
		R.append(r)
		H.append(h)

	rindices = sorted(range(len(R)), key=lambda k: R[k], reverse=True)
	#print(rindices)
	area = 0
	for ri in range(N - K + 1):
		start_r = rindices[ri]
		#print("start_ri", start_r)
		rh = [H[rindices[i]] * R[rindices[i]] for i in range(ri + 1, N)]
		#print(rh)
		srh = sorted(rh, reverse=True)
		#print(srh, R[start_r])

		a = math.pi * (2 * (sum(srh[0:(K - 1)]) + H[start_r]*R[start_r])+ R[start_r] * R[start_r])
		#print(a)
		area = max(area, a)

	gcj.print_answer(ofile, t, area)