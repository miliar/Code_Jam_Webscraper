f = open("in", "rb")
t = int(f.readline())
for tt in range(t):
	print "Case #"+str(tt+1)+":",
	n,l,h = map(int, f.readline().split())
	nn = map(int, f.readline().split())
	y = 0
	for j in range(l, h+1):
		x = 1
		for i in range(n):
			if (nn[i]%j != 0 and j%nn[i]!=0):
				x = 0; break
		if x==1:
			print j; y = 1; break
	if y==0:
		print "NO"	
