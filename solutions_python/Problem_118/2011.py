f = open(raw_input())
T = int(f.readline())

def pal(x):
	y = str(x)
	return all([y[i] == y[len(y)-1-i] for i in xrange(len(y)//2+1)])

# need squares of palindromes to be squares
squares = filter(pal, [x**2 for x in filter(pal, range(32))])
print squares

for t in xrange(T):
	A, B = [int(x) for x in f.readline().strip().split()]
	c = 0
	for fns in squares:
		c += int(A <= fns and fns <= B)
	print "Case #%d: %d" % (t+1, c)

f.close()