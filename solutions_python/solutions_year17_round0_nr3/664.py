def f(n, k):
	while k > 1:
		k -= 1
		if n%2:
			n/=2
			k = k/2+k%2
		else:
			if k%2:
				n/=2
				k = k/2+k%2
			else:
				n=n/2-1
				k/=2
	if n%2:
		return (n/2, n/2)
	else:
		return (n/2-1, n/2)

t=int(raw_input())
tc=0
while t:
	t=t-1
	tc+=1
	s=raw_input().split()
	n, k = int(s[0]), int(s[1])
	z=f(n, k)
	print "Case #"+str(tc)+": "+str(z[1]) + " " + str(z[0])
		