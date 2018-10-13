t = int(input())
for p in range(t):
	a = raw_input()
	n = int(a)
	while n>0:
		k=str(n)
		a = k
		b = list(k)
		k = [int(i) for i in k]
		k.sort()
		k = [str(i) for i in k]
		d="".join(k)
		n-=1
		if str(a) == str(d):
			print "Case #" + str(p+1) + ": " + str(a)
			break

	
