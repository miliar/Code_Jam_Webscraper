def solve(n):
	if n < 10: return n
	digs = list()
	while n > 0:
		digs.append(n%10)
		n /= 10
	digs = digs[::-1]

	for i in range(1, len(digs)):
		if digs[i-1] > digs[i]:
			digs[i-1] -= 1
			for x in range(i, len(digs)):
				digs[x] = 9
			break

	if 0 in digs:
		digs = [9] * (len(digs)-1)
	return int(''.join(map(str, digs)))

if __name__ == '__main__':
	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
		n = int(raw_input())
		print "Case #{}: {}".format(i, solve(n))
 