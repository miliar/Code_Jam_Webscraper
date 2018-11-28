def last_tidy(n):
	n = int(n)
	if n < 10:
		return n
	n = list(str(n))
	for i in range(1, len(n)):
		ii = len(n) - i
		if n[ii] < n[ii-1]:
			return str(last_tidy(int(''.join(n[:ii]))-1)) + '9' * len(n[ii:])
	return ''.join(n)


if __name__ == '__main__':
	import sys
	lines = open(sys.argv[1]).readlines()[1:]
	for i in range(len(lines)):
		n = lines[i].strip()
		print 'Case #{}: {}'.format(i+1, int(last_tidy(n)))
