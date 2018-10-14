def sp(n):
	n-=1
	if (n%2==0): return n//2,n//2
	else: return (n//2)+1, n//2
z = []
for sjdfkjs in range(int(input())):
	n,k = map(int, input().split())
	l = []
	d = k
	while (k!=1):
		if (k%2==1): l.append('r')
		else: l.append('l')
		k//=2
	x, y = sp(n)
	for i in l:
		if i=='l': x, y = sp(x)
		if i=='r': x, y = sp(y)

	z.append(sorted([x,y], reverse=True))
for c,i in enumerate(z): print("Case #" + str(c+1) + ":", i[0], i[1])

