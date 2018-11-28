from fractions import Fraction as F
from math import fsum
T = int(input())
for j in range(T):
	X, S, R, t, N = map(int, input().split())
	BEw = [tuple(map(int, input().split())) for i in range(N)]
	n_by_v = {R: 0}
	for i in range(1, N):
		x = min(t, F(BEw[i][0] - BEw[i-1][1], R))
		n_by_v[R] += x*R
		t -= x
		if not t: break
	if t:
		x = min(t, F(BEw[0][0], R))
		n_by_v[R] += x*R
		t -= x
		x = min(t, F(X - BEw[-1][1], R))
		n_by_v[R] += x*R
		t -= x
	n_by_v[S] = X - sum(i[1]-i[0] for i in BEw) - n_by_v[R]
	BEw = [(i[2], i) for i in BEw]
	BEw.sort()
	for bew in BEw:
		x = min(t, F(bew[1][1] - bew[1][0], bew[0] + R))
		n_by_v[bew[0] + R] = n_by_v.get(bew[0] + R, 0) + x * (bew[0] + R)
		t -= x
		n_by_v[bew[0] + S] = n_by_v.get(bew[0] + S, 0) + bew[1][1] - bew[1][0] - x * (bew[0] + R)
	print('Case #%d: %.6f' % (j+1, fsum(n_by_v[v]/v for v in n_by_v)))