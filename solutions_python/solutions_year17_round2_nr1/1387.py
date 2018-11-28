import sys
sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

for t in range(int(input())):
	d, n = map(int, input().split())

	a = [tuple(map(int, input().split())) for i in range(n)]
	eff = [1 for i in range(n)]

	a.sort(key = lambda x: x[1])

	for k in range(10):
		for i in range(n):
			for j in range(i+1, n):
				if eff[i] and eff[j]:
					a1, b1 = a[i]
					a2, b2 = a[j]
					if b1 == b2:
						continue
					nt = (a1-a2) / (b2-b1)
					md = a1 + b1 * nt
					if nt >= 0 and md < d:
						eff[j] = 0

	r = 0
	for i in range(n):
		if eff[i]:
			x, y = a[i]
			r = max(r, (d-x)/y)

	print('Case #%d: %.8f' % (t+1, d/r))