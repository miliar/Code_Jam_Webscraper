import math
o=int(raw_input())

for ot in range(o):
	n,k=[int(i) for i in raw_input().split()]
	i=0
	c=[1]*n
	c=[0]+c+[0]
	i=0
	j=n
	rx=0
	while k>0:
		mx=0
		pi,pj=0,0
		l=0
		#print mx
		while l<n+1:
			if c[l]==1:
				pi=l
				l+=1
				while c[l]==1:
					l+=1
				pj=l-1
			if mx<=(pj-pi):
				mx=pj-pi
				px=rx
				i=pi
				j=pj
				pi,pj=0,0
				if mx==0:
					while c[px]==0:
						px+=1
					rx=px
					i=px
					j=px
			l+=1
		mx=j-i
		f=float(mx)
		x=i+int(math.ceil(f/2))
		c[x]=0
		k-=1
	a,b=0,0
	p=x
	while c[x-1]==1:
		a+=1
		x-=1
	while c[p+1]==1:
		b+=1
		p+=1
	print "Case #%d: %d %d" % (ot+1, a,b)
