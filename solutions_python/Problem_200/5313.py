n=int(raw_input())
def tidy(x):
	xx=list(x)
	xxx=sorted(xx,key=int)
	a=''.join(map(str,xx))
        b=''.join(map(str,xxx))
	if a==b:
		return True
for i in range(n):
	z=raw_input()
	x=int(z)
	if len(z)==1:
		print "Case #%d: %d"%(i+1,x)
	else:
		while tidy(str(x))!=True:
				x=x-1
		print "Case #%d: %d"%(i+1,x)
			
		
	
