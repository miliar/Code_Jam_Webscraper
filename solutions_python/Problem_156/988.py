def calc(x,y):
	r=len(x)
	x=x*len(y)
	w=-1
	s=y[0]
	for q in xrange(len(x)):
		if q%r ==0:
			w=w+1
			s=y[w]
		x[q]=[max(x[q][0],s[0]),x[q][1]+s[1]]
	return x

t=input()
d={}
d[9]=[[3,2],[5,1],[9,0]]
d[8]=[[4,1],[8,0]]
d[7]=[[4,1],[7,0]]
d[6]=[[3,1],[6,0]]
d[5]=[[3,1],[5,0]]
d[4]=[[2,1],[4,0]]
d[3]=[[3,0]]
d[2]=[[2,0]]
d[1]=[[1,0]]
for i in xrange(t):
	a=input()
	b=map(int,raw_input().split())
	#print b
	x=d[b[0]]
	#print "Initail x is ",x
	for j in xrange(1,a):
		y=d[b[j]]
		#print j,x,"first one ",y
		x=calc(x,y)
		#print j,x,"second one ",y
		#print
	z=[]
	for j in x:
		z.append(j[0]+j[1])
	print "Case #%d: %d" %(i+1,min(z))
		
	
	
	
