
def main():
	t = input()
	for i in xrange(1, t+1):
		print 'Case #%d: %.7f' % (i, solve())

def solve():
	# Get the result of the game
	c, f, x = map(float, raw_input().split())
	r, t = 2, 0.0
	while buy(c, f, x, r):
		t += c / r
		r += f
	t += x / r
	return t

def buy(c, f, x, r):
	# whether to buy a farm or not
	return ((c / x) + (r / (f+r))) < 1

	
if __name__ == '__main__':
	main()