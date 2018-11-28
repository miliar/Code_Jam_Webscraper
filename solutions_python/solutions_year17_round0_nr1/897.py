FAIL = "IMPOSSIBLE"

def flip(c):
	if c == '+': return '-'
	if c == '-': return '+'


def n_flip(cakes, n, idx):
	assert idx + n <= len(cakes)

	to_return = cakes[:idx]
	for i in range(n):
		to_return += flip(cakes[idx + i])
	to_return += cakes[idx + n:]
	return to_return

def solve(cakes, n):
	if not '-' in cakes:
		return 0
	flips = 0
	idx = 0
	while ('-' in cakes or cakes.count('-') == 1) and idx < 10:
		idx += 1
		first = cakes.find('-')
		cakes = n_flip(cakes, n, first)
		flips += 1

	if cakes.count('-') == 1:
		return IMPOSSIBLE
	if not '-' in cakes:
		return flips
	raise IOError(cakes)


with open('A-small-attempt0.in') as f:
	num_cases = int(f.readline())
	for i in range(num_cases):
		line = f.readline()
		cakes = line.split(' ')[0]
		flipper = int(line.split(' ')[1].strip())
		try:
			result = solve(cakes, flipper)
		except Exception, e:
			result = FAIL
		print "Case #{}: {}".format(i + 1, result)