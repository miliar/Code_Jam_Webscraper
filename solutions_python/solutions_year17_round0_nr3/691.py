def solve(n, k):
	l = k.bit_length()
	p = 1 << (l-1)
	# print(p)
	i = int((n-k+p)//p)-1
	# print((n-k+p)//p)
	# print(i)
	b = int(i//2)
	a = i-b
	return "{0} {1}".format(a, b)

# print(solve(999999999999999999, 1))


if __name__ == '__main__':
	fname = 'C-large.in'
	oname = 'p3.out'
	f = open(fname, 'r')
	g = open(oname, 'w+')
	first = True
	case = 1
	for line in f:
		ans = "IMPOSSIBLE"
		if first: first = False
		else:
			strs = line.split(' ')
			a = solve(int(strs[0]), int(strs[1]))
			if a is not None: ans = a
			g.write("Case #{0}: {1}\n".format(str(case), str(ans)))
			case+=1