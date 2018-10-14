def check(a, b):
	x = str(a)
	len_a = len(x)
	c = 0
	i = 0
	use = {}
	while i < len_a:
		y = ''
		j = 0
		while j < len_a:
			y += x[(i+j)%len_a]
			j += 1
		if a < int(y) <= b and int(y) not in use:
			use[int(y)] = 1
			c += 1
		i += 1
	return c

def solve(a, b):
	count = 0
	for x in range(a, b):
		count += check(x, b)
	return count

n = int(raw_input().strip())
for x in range(n):
	a, b = [int(y) for y in raw_input().strip().split()]
	print 'Case #%d: %d' %(x+1, solve(a, b))
