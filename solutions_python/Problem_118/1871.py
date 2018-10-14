from math import sqrt

def calc(a, b):
	lower = int(sqrt(a))
	if lower < sqrt(a): lower += 1
	upper = int(sqrt(b))
	counter = 0
	for i in xrange(lower, upper+1):
		counter += check(i) and 1 or 0
	return counter

def check(i):
	s = str(i)
	r = s == s[::-1]
	if r:
		ss = str(i*i)
		return ss == ss[::-1]

def main():
	nl = int(raw_input())
	n = 0
	inp = []
	for i in range(nl):
		n += 1
		a,b = map(int, raw_input().split())
		print "Case #%d: %d" %(n, calc(a, b))

main()