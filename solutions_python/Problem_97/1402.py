inp=file('LCinp','r')
l=inp.readlines()
intl=map(lambda x: map(lambda y: int(y),x.split()),l)
#print intl

listmover=0;

for w in xrange(1,intl[0][0]+1):
	a,b=intl[w][0],intl[w][1]
	count=0
	for i in xrange(a,b+1):
		s=str(i)
		repete=[]
		for j in xrange(1,len(s)):
			temp=s[len(s)-j:]+s[:len(s)-j]
			if int(temp)>i and int(temp)<b+1 and int(temp)>a+1 and temp[0]!='0':
				try:
					repete.index(temp)
					#print "repeat"
				except ValueError:
					count=count+1
					repete.append(temp)
	print "Case #"+str(w)+":",count
			
