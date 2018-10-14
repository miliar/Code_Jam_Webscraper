T=int(raw_input().strip())
for _ in xrange(T):
	print "Case #"+str(_+1)+":",
	a=list(raw_input().strip())

	temp=[]
	for i in xrange(len(a)-1):
		if int(a[i])>int(a[i+1]):
			k=i+1
			while k<len(a):
				a[k]='9'
				k+=1 
			j=i
			while j>0 and int(a[j])-1<int(a[j-1]):
				a[j]='9'
				j-=1
			a[j]=str(int(a[j])-1)
			break
	
	print "".join(a).strip('0')		
