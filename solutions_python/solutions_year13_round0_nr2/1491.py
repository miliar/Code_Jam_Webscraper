def check(row, col, ls, n):
	temp = []
	for i in ls:
		tempr = []
		for j in i:
			if j == 2:
				tempr.append(True)
			else:
				tempr.append(False)
		temp.append(tempr)
	# print temp
	r = range(row)
	for i in r:
		if same(ls[i]):
			temp[i] = [True]*col
	# print temp
	for j in xrange(col):
		if same(map(lambda x: x[j], ls)):
			for i in r:
				temp[i][j] = True

	if all(map(all, temp)):
		print "Case #%d: YES" %n
	else:
		print "Case #%d: NO" %n

def same(xs):
	if len(xs) > 1:
		return xs[0] == xs[1] and same(xs[1:])
	else:
		return True

def main():
	nl = int(raw_input())
	n = 0
	for i in xrange(nl):
		n += 1
		inp = []
		row, col = map(int, raw_input().strip().split())
		for r in xrange(row):
			inp.append(map(int, raw_input().strip().split()))
		check(row, col, inp, n)

main()