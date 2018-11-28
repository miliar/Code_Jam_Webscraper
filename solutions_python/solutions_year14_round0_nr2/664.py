DEBUG = False

def shouldBuy(x, c, r, C, F):
	return (x-c+C)/(r+F) < (x-c)/float(r)

def nextTime(c, r, C, x):
	return min((C-c)/r, (x-c)/float(r))

def solve(C, F, X):
	t = 0.0
	c = 0.0
	r = 2.0

	#print locals()
	#print shouldBuy(X, c, r, C, F)

	while c < X:
		if c >= C:
			if (not shouldBuy(X, c, r, C, F)):
				if DEBUG:
					print locals()
					print "not buying - waiting"
				return t + (X-c)/float(r)
			else:
				if DEBUG:
					print locals()
					print "buying"
				c -= C
				r += F
		else:
			if DEBUG:
				print locals()
				print "waiting to buy"
			n = nextTime(c, r, C, X)
			t += n
			c += r*n
		if DEBUG:
			print "---"
	return t

def main():
	T = int(raw_input())
	for t in xrange(1, T+1):
		C, F, X = map(float, raw_input().split())
		print 'Case #{0}: {1:1.7f}'.format(t, solve(C, F, X))

if __name__ == '__main__':
	main()
