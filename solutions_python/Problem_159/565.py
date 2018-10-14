def solve(N, m):
	a = 0
	bd = 0
	for i,v in enumerate(m):
		if len(m) == i+1:
			break
		t = m[i] - m[i + 1]
		if t > 0:
			a += t
			if t > bd:
				bd = t

	b = 0
	for i,v in enumerate(m):
		if len(m) == i + 1:
			break
		if v < bd:
			b += v
		else:
			b += bd

	return (a, b)
		
			
if __name__ == '__main__':
	f = open('input')
	T = int(f.readline().rstrip())
	for case in range(T):
		N = f.readline().rstrip()
		m = list(map(int, f.readline().rstrip().split(' ')))
		r = solve(N, m)
		print('Case #{0}: {1} {2}'.format(case+1, r[0], r[1]))
