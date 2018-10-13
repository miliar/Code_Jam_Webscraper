import itertools
for i in range(input()):
	n, k = map(int, raw_input().split())
	d = {n: 1}
	while 1:
		x = max(d.keys())
		y = d[x]
		a = x / 2
		b = (x - 1) / 2
		if k >= y:
			del d[x]
			k -= y
			d[a] = d.setdefault(a, 0) + y
			d[b] = d.setdefault(b, 0) + y
			if k == 0:
				break
		else:
			break
	print "Case #" + str(i + 1) + ": " + str(a) + " " + str(b)
