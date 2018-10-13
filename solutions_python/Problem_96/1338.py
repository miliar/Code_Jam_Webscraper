"""

0 0 1


"""

from sys import stdin

cases = int(stdin.readline())

for case in xrange(cases):
	nums = [int(x) for x in stdin.readline().split(' ')]
	S = nums[1]
	p = nums[2]
	del nums[0:3]
	pcount = 0
	for x in nums:
		(base, left) = (x/3, x%3)
		basep1 = base + 1
		basep2 = base + 2

		if base>=p or (left>=1 and basep1>=p):
			pcount += 1
			continue

		if left == 1 or S <= 0:
			continue

		if left == 0 and basep1>=p and base > 0:
			pcount += 1
			S -= 1

		if left == 2 and basep2>=p:
			pcount += 1
			S -= 1


	print 'Case #%d: %d' % (case+1, pcount)
