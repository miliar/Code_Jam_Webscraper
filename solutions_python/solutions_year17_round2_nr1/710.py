def f(l, d):
	l.sort(key=lambda x: x[0], reverse=True)
	prd, prs = l[-1]
	t = (d - prd) / prs
	ami = d / t
	for i in range(n-2, -1, -1):
		di, si = l[i]
		dii = t * prs
		t = (prd + dii - di) / si
		s = d / t
		if s < ami:
			ami = s
		prd, prs = di, si
	return ami

t = int(input())
for it in range(1, t+1):
	d, n = map(int, input().split())
	l = []
	for i in range(n):
		k, s = map(int, input().split())
		l.append((k, s))
	print("Case #%d:" % it, f(l, d))
