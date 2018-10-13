t = int(input())

p=1
while p<=t:
	n = int(input())
	a = []
	i = 0
	while i<n:
		if (n-i) == int("".join(sorted(str(n-i)))):
			a.append(n-i)
		i = i+1
	print("Case #%d: %d"%(p,a[0]))
	p = p+1

