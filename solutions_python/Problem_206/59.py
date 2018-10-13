Cases = int(input())
for Case in range(Cases):
	d, n = map(int,input().split())
	h = []
	for i in range(n):
		kk,ss = map(int,input().split())
		h.append((kk,ss))
	h.sort()
	# print(h)

	t = 0
	for k,s in reversed(h):
		t = max(t, (d-k)/s)

	print('Case #%d: %.6f' % (Case+1, d/t))