import sys, math

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	i=1
	while i <= n:
		# ignore next stdin line...number of diners with non-empty plates
		sys.stdin.readline()

		pancakes = [int(x) for x in sys.stdin.readline().split()]
		pancakes.sort(reverse=True)

		ans = float('inf')

		for rnd in xrange(1, pancakes[0] + 1):
			special_round = 0
			for pancacke in pancakes:
				if pancacke <= rnd:
					break
				special_round += math.ceil(pancacke*1.0/rnd)
				special_round -= 1
			if special_round + rnd < ans:
				ans = special_round + rnd
		
		print 'Case #%d: %d' % (i, ans)
		i+=1
