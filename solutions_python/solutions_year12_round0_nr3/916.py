def check(x,y):
	x = str(x)
	y = str(y)
	
	for i in xrange(len(x)):
		if(x[i:]+x[:i] == y): 
			return 1
	
	
	return 0
	
tc= int(raw_input())

for i in xrange(tc):
	a,b = map(int,raw_input().split(' '))
	ret=0
	
	
	for x in xrange(a,b+1):
		for y in xrange(x+1,b+1):
			ret += check(x,y)
	print "Case #"+str(i+1) +":",ret
		
