import sys


te = input()

for qe in range(1, te+1):

	d, n = map(int, raw_input().split())

	ans = 99999999999999999

	for _ in range(n):
		k, s = map(int, raw_input().split())
		ans = min(ans, d*s*1.0/(d-k))

	print >> sys.stderr, str(qe)+'/'+str(te)+' started ...'

	print 'Case #{}: {:.7f}'.format(qe, ans)