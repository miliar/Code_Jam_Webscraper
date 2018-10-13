import sys

def fakePlus(x, y):
	bx = bin(x)
	bx = bx[2:]
	by = bin(y)
	by = by[2:]

	while len(bx) < len(by): bx = '0' + bx
	while len(by) < len(bx): by = '0' + by

	ans = 0
	for i in range(0, len(bx)):
		re = 1
		if bx[i] == by[i]: re = 0
		ans = ans + pow(2, len(bx) - i - 1)*re

	return ans

def fakeMinus(x, y):
	bx = bin(x)
	bx = bx[2:]
	by = bin(y)
	by = by[2:]

	while len(bx) < len(by): bx = '0' + bx
	while len(by) < len(bx): by = '0' + by

	ans = 0
	for i in range(0, len(bx)):
		re = 1
		if bx[i] == by[i]: re = 0
		ans = ans + pow(2, len(bx) - i - 1)*re

	return ans

fi = open("input.txt", "r")
fo = open("output.txt", "w")

c = int(fi.readline().strip());
for tc in range(1, c + 1):
	tmp = list(map(int, fi.readline().strip().split(" ")))
	n = tmp[0]
	a = list(map(int, fi.readline().strip().split(" ")))
	free = [True]*n

	ftotal = 0
	total = 0
	for i in range(0, n):
		ftotal = fakePlus(ftotal, a[i])
		total = total + a[i]


	ans = [0]

	def attemp(k, b, r, rb, rr):
		orgb = b
		orgr = r
		orgrb = rb
		orgrr = rr
		for i in range(k, n):
			if free[i]:
				b = fakePlus(orgb, a[i])
				r = fakeMinus(orgr, a[i])
				rb = orgrb + a[i]
				rr = orgrr - a[i]

				if b == r and rb <> 0 and rr <> 0:
					#ans.append(max(rb, rr))
					if max(rb, rr) > ans[0]:
						ans[0] = max(rb, rr)

				free[i] = False
				attemp(i + 1, b, r, rb, rr)
				free[i] = True

	attemp(0, 0, ftotal, 0, total)
	if ans[0] > 0:
		ans = max(ans)
	else: ans = 'NO'
						
	fo.write("Case #{0}: {1}\n".format(tc, str(ans)))
	
fi.close()
fo.close()