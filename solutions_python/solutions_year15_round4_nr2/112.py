
def solveOne(v, x, r, c):
	if abs(c - x) < 1e-6:
		return '{0:.10f}'.format(v/r)
	else:
		return 'IMPOSSIBLE'

def solve():
	line = raw_input().split(' ')
	n = int(line[0])
	v = float(line[1])
	x = float(line[2])
	r1, c1 = map(float, raw_input().split(' '))
	if n == 2:
		r2, c2 = map(float, raw_input().split(' '))

		if (c1 < x and c2 < x) or (c1 > x and c2 > x):
			return 'IMPOSSIBLE'

		if abs(c1 - c2) < 1e-6:
			return solveOne(v, x, r1+r2, c1)

		t1 = v * (x - c2) / r1 / (c1 - c2)
		t2 = v * (x - c1) / r2 / (c2 - c1)

		return '{0:.10f}'.format(max(t1, t2))
	else:
		return solveOne(v, x, r1, c1)


def main():
	t = int(raw_input())
	for tt in range(t):
		print 'Case #{0}: {1}'.format(tt+1, solve())

if __name__ == '__main__':
	main()