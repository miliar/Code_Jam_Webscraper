import sys


te = input()

for qe in range(1, te+1):

	ac, aj = map(int, raw_input().split())

	c = [map(int, raw_input().split()) for _ in range(ac)]
	j = [map(int, raw_input().split()) for _ in range(aj)]


	if ac+aj == 1:
		ans = 2
	elif ac*aj == 1:
		ans = 2
	else:
		if aj == 2:
			c = j

		l = min(c[0][0], c[1][0])
		r = 1440 - max(c[0][1], c[1][1])

		if l+r>=720:
			ans = 2
		elif c[0][1]-c[0][0] + c[1][1]-c[1][0] + l + r <= 720:
			ans = 2
		else:
			ans = 4 


	print >> sys.stderr, str(qe)+'/'+str(te)+' started ...'

	print 'Case #{}: {}'.format(qe, ans)