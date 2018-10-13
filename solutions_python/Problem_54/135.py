import sys

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return a * b / gcd(a,b)

def solve(P):
	line = sys.stdin.readline().split()
	assert len(line) == int(line[0]) + 1
	years = map(int, line[1:])
	years.sort()
	common = reduce(gcd, [ y - years[0] for y in years])
	if len(filter(lambda x : x % common == 0, years)) == len(years):
		print 'Case #%d: %d' % (P, 0)
	else:
		print 'Case #%d: %d' % (P, reduce(lcm, [ common - (y % common) for y in years if y % common != 0]))

def main():
	n = int(sys.stdin.readline())
	for i in xrange(n):
		solve(i+1)

if __name__ == '__main__':
	main()
