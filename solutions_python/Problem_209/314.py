import sys
import math


te = input()

for qe in range(1, te+1):

	n, k = map(int, raw_input().split())

	# r = [0]*n
	# h = [0]*n
	x = [0]*n

	for i in range(n):
		x[i] = map(int, raw_input().split())
	

	ans = 0


	for i in range(n):
		f = math.pi * (x[i][0] ** 2) + 2*math.pi*x[i][0]*x[i][1]
		s = 2 * math.pi * sum(map(lambda l: l[0]*l[1], sorted(x[:i]+x[i+1:], key=lambda r: r[0]*r[1], reverse=True) [:k-1]))
		ans = max(ans, f+s)

	print >> sys.stderr, str(qe)+'/'+str(te)+' started ...'

	print 'Case #{}: {:.9f}'.format(qe, ans)