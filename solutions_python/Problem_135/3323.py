
def main():
	t = input()
	for i in xrange(1, t+1):
		print 'Case #%d: %s' % (i, solve())

def solve():
	# Get the result of the trick
	c = cards() & cards()
	if len(c) == 1:
		return '%d' % c.pop()
	elif len(c) > 1:
		return 'Bad magician!'
	else:
		return 'Volunteer cheated!'

def cards():			
	# return the row volunteer selected and discard the rest
	r = input() - 1
	c = set()
	for i in xrange(4):
		if r == i:
			c = set(map(int, raw_input().split()))
		else:
			raw_input()
	return c

	
if __name__ == '__main__':
	main()