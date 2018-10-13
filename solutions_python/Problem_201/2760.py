T = input()
for t in range(T):
	n,k = map(int,raw_input().split())
	a=100000
	b=0
	x = [n]
	while k>0:
		k -=1
		x.sort()
		y = x.pop()
		a = y/2
		b = y/2+(y%2-1)
		x.append(a)
		x.append(b)
	print "Case #"+str(t+1)+": "+ str(max(a,b)) + " " + str(min(a,b))

