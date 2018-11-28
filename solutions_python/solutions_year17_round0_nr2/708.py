def solve(n):
	l = list(str(n))
	start = 0
	for i in range(len(l)-1):
		if int(l[i]) < int(l[i+1]):
			start = i+1
		elif int(l[i]) > int(l[i+1]):
			l[start] = str(int(l[start])-1)
			for j in range(start+1, len(l)):
				l[j] = '9'
			break
	return int(''.join(l))

# print(solve(111111111110))

if __name__ == '__main__':
	fname = 'B-large.in'
	oname = 'p2.out'
	f = open(fname, 'r')
	g = open(oname, 'w+')
	first = True
	case = 1
	for line in f:
		ans = "IMPOSSIBLE"
		if first: first = False
		else:
			a = solve(int(line))
			if a is not None: ans = a
			g.write("Case #{0}: {1}\n".format(str(case), str(ans)))
			case+=1