import sys

def is_recycled(n, m):
	n_str = str(n)
	if n < m:
		for i in range(len(n_str)-1):
			n_str = n_str[-1] + n_str[:-1]
			if int(n_str) == m:
				return True

	return False


if __name__ == '__main__':
	f = open(sys.argv[1])

	t = f.readline()
	i = 1
	for line in f.readlines():
		a, b = line.split()

		a = int(a)
		b = int(b)

		count = 0

		for n in range(a, b):
			for m in range(n+1, b+1):
				if is_recycled(n, m):
					count += 1

		print "Case #{}: {}".format(i, count)
		i += 1
