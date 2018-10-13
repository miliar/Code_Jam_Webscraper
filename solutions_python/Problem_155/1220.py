import sys

def main():
	T = int(sys.stdin.readline())
	c = 1
	while T > 0:
		smax, str = sys.stdin.readline().split()
		smax = int(smax)
		currStanding = 0
		need = 0
		for k in xrange(smax+1):
			if currStanding < k:
				need += k - currStanding
				currStanding = k
			currStanding += int(str[k])
		print 'Case #{0}: {1}'.format(c, need)
		c += 1
		T -= 1

if __name__ == '__main__':
	main()
