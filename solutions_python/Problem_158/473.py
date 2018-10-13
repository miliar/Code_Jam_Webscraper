T = int(raw_input())

for test in range(1, T+1):
	x, r, c = map(int, raw_input().split())

	grids = r*c

	possible = False

	if x > grids:
		possible = False
	elif grids % x != 0:
		possible = False
	else:
		if x == 1:
			possible = True
		elif x == 2:
			possible = (r%2 == 0 or c%2 == 0)
		elif x == 3:
			possible = max(r,c) > 2 and min(r, c) > 1
		else:
			possible = max(r,c) == 4 and min(r,c) >= 2

			if possible:
				possible = not(max(r,c) == 4 and min(r,c) == 2)

	print "Case #{}: {}".format(test, "GABRIEL" if possible else "RICHARD")
