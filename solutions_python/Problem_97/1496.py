from sys import argv
import itertools

def cycle(n):
	result = [n]
	s = str(n)
	for i in xrange(1, len(s)):
		cycled = s[i:] + s[:i]
		result.append(int(cycled))
	return set(result)

def case(a, b):
	known = set([])
	result = 0

	for n in xrange(a, b+1):
		if n in known:
			continue
		c = cycle(n)
		for m in c:
			known.add(m)
		for (n,m) in itertools.product(c, c):
			if a <= n < m <= b:
				result += 1

	return result

if __name__ == "__main__":
	with open(argv[1], 'r') as f:
		lines = f.readlines()
	assert int(lines[0]) == len(lines) - 1
	lines = lines[1:]

	i = 1
	for line in lines:
		[a, b] = [int(n) for n in line.rstrip().split(" ")]
		print "Case #{}: {}".format(i, case(a, b))
		i += 1
