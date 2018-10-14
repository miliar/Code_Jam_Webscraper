def case():
	(n, A, B, C, D, x0, y0, M) = [int(x) for x in raw_input().split(' ')]
	x, y = x0, y0
	xs, ys = [x], [y]
	for i in range(1, n):
		x = (A * x + B) % M
		y = (C * y + D) % M
		xs.append(x)
		ys.append(y)
	print sum(1 for (x1, y1) in zip(xs, ys) for (x2, y2) in zip(xs, ys) for (x3, y3) in zip(xs, ys) if (x1 + x2 + x3) % 3 == 0 and (y1 + y2 + y3) % 3 == 0 and (x1 != x2 or y1 != y2) and (x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3)) / 6

ncases = int(raw_input())
for i in range(ncases):
	print "Case #" + str(i+1) + ":",
	case()
