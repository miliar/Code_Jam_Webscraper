def solve(n, k):
	#print "solve(" + str(n) + ", " + str(k) + ")"
	n -= 1
	k -= 1
	ls = n/2
	rs = (n/2) + (n&1)
	if k == 0:
		return ( n/2, (n/2)+(n&1) )

	if (k&1) == 1:
		return solve(rs, (k/2) + (k&1))
	else:
		return solve(ls, k/2)
	#print n
	return solve(n, k)


t = int(raw_input())

for q in range(t):
	[n, k] = map(int, raw_input().split(' '))
	z,y = solve(n,k)
	print "Case #" + str(q+1) + ": " + str(y) + " " + str(z)