import heapq
 
t=int(raw_input())
i=1
while i<=t:
	i+=1
	d=int(raw_input())
	temp=raw_input()

	p=[]
	temp=temp.split(' ')
	for x in temp:
		p.append(int(x))
	maxim=max(p)
	mincnt=0
	j=1
	while j<=maxim:
		minr=0
		divides=0
		k=0
		l=len(p)
		while k<l:
			if j>=p[k]:
				minr=max(minr,p[k])
			else:
				divides+=p[k]/j
				if p[k]%j==0:
					divides-=1

				if j==max(minr,j):
					minr=j
			k+=1
		if j==1 or (minr+divides<=mincnt):
			mincnt=minr+divides
		j+=1
	print "Case #"+str(i-1)+": "+str(mincnt)
