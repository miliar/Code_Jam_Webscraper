t = input()
def getanothernum(Lis):
	Lis = [str(i) for i in Lis]
	s = ''.join(Lis)
	
	if( int(s) == 0):
			return 1
	else:
		return int(s)
for x in xrange(t):
	num = input()
	ans = False
	while(num != 0):
		numlist = [int(i) for i in str(num)]
		forbreak = False
		for y in xrange(0,len(numlist)-1):
			if(numlist[y] > numlist[y+1]):
				
				num-= getanothernum(numlist[y+1: ])
				
				forbreak = True
				break
		if(forbreak):
				1+1
		else:
			print "Case #" + str(x+1) + ": "+ str(num)
			break