t = int(input())
for z in range(t):
	n = list(map(int,list(input())))
	a = len(n)
	for i in range(1,a):
		if (n[a-i] < n[a-i-1]):
			for j in range(a-i,a):
				n[j] = 9
			n[a-i-1] -= 1
	b = ''
	for i in range(a):
		b += str(n[i])

	print ("Case #%s: %s" %(z+1,int(b)))
