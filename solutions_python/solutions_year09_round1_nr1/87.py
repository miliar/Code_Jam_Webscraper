def convert(n, b):
	dig = []
	while n != 0:
		dig.append(n%b)
		n /= b
	dig.reverse()
	return reduce(lambda a, b: (a+b)*10, dig, 0) / 10
	
def happy(n, b):
	nb = convert(n, b)
	d = {}

	while nb > 1:
		d[nb] = True
		nb = reduce(lambda x, y: x+y, map(lambda x: int(x)**2, list(str(nb))), 0)
		nb = convert(nb, b)

		if d.has_key(nb):
			return 0

	return nb

def solve(bases, case):
	i = 2
	while True:
		hap = True
		for j in bases:
			if not happy(i, j):
				hap = False
				break
		if hap:
			print "Case #%d: %d" % (case, i)
			break
		i += 1
		
n = input()
for i in range(n):
	solve(map(int, raw_input().split()), i+1)