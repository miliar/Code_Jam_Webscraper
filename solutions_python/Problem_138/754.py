from sys import stdin




t=int(stdin.readline())
for case in xrange(t):
	n = int(stdin.readline())
	a = stdin.readline()
	a  = map(float, a.split())
	b=stdin.readline()
	b=map(float,b.split())
	a.sort()
	b.sort()
	without_cheat = 0
	with_cheat = 0
	first = n-1
	second_low = 0
	second_hi = n-1
	for i in xrange(n):
		cur = a[first]
		first-=1
		if b[second_hi ]>= cur:
			second_hi-=1
		else:
			without_cheat+=1
			second_low+=1
	first = 0
	second_low = 0
	second_hi = n-1
	for i in xrange(n):
		cur = a[first]
		if cur > b[second_low]:
			with_cheat+=1
			second_low+=1
		else:
			if cur > b[second_hi]:
				with_cheat+=1
			second_hi-=1
		first+=1
	
	
	print "Case #%d: %d %d"%(case+1, with_cheat, without_cheat)



















#print "Case #%d: %.12lf"%((case+1),res)