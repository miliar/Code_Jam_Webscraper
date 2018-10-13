class V(tuple):
	__slots__ = ()
	def __add__(a, b):
		return V((a[0] + b[0], a[1] + b[1]))
	def __sub__(a, b):
		return V((a[0] - b[0], a[1] - b[1]))
	def __mul__(self, coef):
		return V((self[0] * coef, self[1] * coef))
T = int(input())
for iT in range(1, T+1):
	R, C, D = map(int, input().split())
	w = [tuple(map(int, input().strip())) for i in range(R)]
	pm1, pm, m = [], [[V((0, 0))] * (C+1)], [[0] * (C+1)]
	for i in range(R):
		pm1r, pmr, mr = [], [V((0, 0))], [0]
		for j in range(C):
			mr.append(mr[-1] + m[-1][j+1] - m[-1][j] + w[i][j])
			pm1r.append(V((i, j)) * w[i][j])
			pmr.append(pmr[-1] + pm[-1][j+1] - pm[-1][j] + pm1r[-1])
		pm1.append(pm1r)
		pm.append(pmr)
		m.append(mr)
	for ans in range(min(C, R), 2, -1):
		half = ans >> 1
		if ans & 1:
			for i in range(half, R - half):
				for j in range(half, C - half):
					spm = pm[i+half+1][j+half+1] + pm[i-half][j-half] - pm[i+half+1][j-half] - pm[i-half][j+half+1] - pm1[i+half][j+half] - pm1[i+half][j-half] - pm1[i-half][j+half] - pm1[i-half][j-half]
					sm = m[i+half+1][j+half+1] + m[i-half][j-half] - m[i+half+1][j-half] - m[i-half][j+half+1] - w[i+half][j+half] - w[i+half][j-half] - w[i-half][j+half] - w[i-half][j-half]
					if spm == V((i, j)) * sm:
						break
				else:
					continue
				break
			else:
				continue
			break
		else:
			for i in range(half, R - half + 1):
				for j in range(half, C - half + 1):
					spm = pm[i+half][j+half] + pm[i-half][j-half] - pm[i+half][j-half] - pm[i-half][j+half] - pm1[i+half-1][j+half-1] - pm1[i+half-1][j-half] - pm1[i-half][j+half-1] - pm1[i-half][j-half]
					sm = m[i+half][j+half] + m[i-half][j-half] - m[i+half][j-half] - m[i-half][j+half] - w[i+half-1][j+half-1] - w[i+half-1][j-half] - w[i-half][j+half-1] - w[i-half][j-half]
					if spm == V((i-.5, j-.5)) * sm:
						break
				else:
					continue
				break
			else:
				continue
			break
	else:
		print('Case #%d: IMPOSSIBLE' % iT)
		continue
	print('Case #%d: %d' % (iT, ans))