t = int(input())

def level(n,a,l):
	if (a == 0):
		return l

	else:
		if (n%2 == 0):
			b = n//2
			l.append(b)
			level(b,a-1,l)
			l.append(b- 1)
			level(b-1,a-1,l)

		else:
			b = n//2
			l.append(b)
			level(b,a-1,l)
			l.append(b)
			level(b,a-1,l)



for z in range(t):
	n,k = map(int,input().split())
	l = [n]
	a = len("{0:b}".format(k)) - 1
	level(n,a,l)
	l.sort(reverse=True)
	x = l[k-1]
	if (x%2 == 0):
		print ("Case #%s: %s %s" %(z+1,x//2,x//2-1))
	else:
		print ("Case #%s: %s %s" %(z+1,x//2,x//2))
