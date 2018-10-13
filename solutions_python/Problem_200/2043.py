def solve(n):
	l = len(n)
	for i in range(1, l):
		x = int(n[i-1])
		d = int(n[i])
		if d < x:
			for j in range(i, l):
				n[j] = '9'
			n[i-1] = str(x-1)

			for k in range(i-1, 0, -1):
				xx = int(n[k-1])
				dd = int(n[k])
				if dd < xx:
					n[k] = '9'
					n[k-1] = str(xx-1)

	return int(''.join(n))
	

t = int(input())
for case in range(1, t+1):
	n = list(input())
	res = solve(n)
	print("Case #%i: %i" % (case, res))
