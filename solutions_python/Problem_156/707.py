def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

def solve(P, t):
	pmax = 0
	for i in xrange(len(P)):
		if P[i] > 0:
			pmax = i

	if pmax <= 3:
		return pmax + t


	m2 = pmax/2
	m3 = pmax/3
	p = P[pmax]
	P[pmax] = 0
	P1 = list(P)

	P[m2] += p
	P[pmax-m2] += p
	P1[m3] += p
	P1[pmax-m3] += p

	return min(pmax+t, solve(P, t+p), solve(P1, t+p))


def T(n, time):
	if time[n]:
		return time[n]
	if n in [0, 1, 2]:
		val = n
	elif n%2 == 0:
		val = T(n/2, time) + 1
	else:
		val = 1 + T(n-1, time)

	time[n] = val
	return val

_T = readint()

for _t in range(_T):
	print('Case #%i:'%(_t+1)),

	D = readint()
	P =  [0] * 10
	for p in readarray(int):
		P[p] += 1

	print solve(P, 0)

