T = int(input())
for t in range(T):
	d, n = map(int, input().split())
	a = []
	b = []
	for i in range(n):
		aa, bb = map(int, input().split())
		a.append(aa)
		b.append(bb)
	
	aas = []
	for i in range(len(a)):
		aas.append((d - a[i]) / b[i])
	
	ans = 0
	for i in range(1, len(aas)):
		if aas[i] > aas[ans]:
			ans = i
	
	print("Case #", end = '')
	print(t + 1, end = '')
	print(': ', end = '')
	print(format(d / aas[ans], ".6f"))
