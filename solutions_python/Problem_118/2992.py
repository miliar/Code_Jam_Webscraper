cases=input()
for i in xrange(1,cases+1):
	the_string = raw_input()
	initial,final=the_string.split()
	count=0
	for x in xrange(int(initial),int(final)+1):
		temp=x
		temp=str(temp)
		if temp==temp[::-1]:
			sqr=x**(0.5)
			if sqr==(sqr//1):
				sqr=str(int(sqr))
				if(sqr==sqr[::-1]):
					count=count+1
	j="Case #"+str(i)+":"
	print j, count