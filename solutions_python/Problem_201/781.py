def f(n, k):

	if k == 0:
		return n

	if n%2 == 1:

		return f(n/2, (k-1)/2)

	elif k%2 == 1:

		return f(n/2, k/2)

	else:

		# a = f(n/2, k/2)
		c = f((n-1)/2, (k-1)/2)

		# return max(a,c)
		return c


t = input()

for qe in range(1, t+1):

	n, k = map(int, raw_input().split())
	
	a = f(n, k-1)
	print 'Case #{}: {} {}'.format(qe, a/2, (a-1)/2)