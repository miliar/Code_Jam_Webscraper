def solve():
	n, v, x = input().split()
	n = int(n)
	v = int(v.replace('.', ''))
	x = int(x.replace('.', ''))
	if n == 1:
		r, c = input().split()
		r = int(r.replace('.', ''))
		c = int(c.replace('.', ''))
		if c == x:
			return v / r
		return 'IMPOSSIBLE'
	r1, c1 = input().split()
	r2, c2 = input().split()
	r1 = int(r1.replace('.', ''))
	c1 = int(c1.replace('.', ''))
	r2 = int(r2.replace('.', ''))
	c2 = int(c2.replace('.', ''))
	if c1 == c2:
		r = r1 + r2
		c = c1
		if c == x:
			return v / r
		return 'IMPOSSIBLE'
	a = r1
	b = r2
	c = r1 * c1
	d = r2 * c2
	det = a * d - b * c
	if det == 0:
		return 'IMPOSSIBLE'
	det1 = v * d - b * x * v
	det2 = a * x * v - v * c
	t1 = det1 / det
	t2 = det2 / det
	if t1 < -1e-8 or t2 < -1e-8:
		return 'IMPOSSIBLE'
	return max(t1, t2)

t = int(input())
for i in range(t):
	print('Case #{}: {}'.format(i + 1, solve()))
