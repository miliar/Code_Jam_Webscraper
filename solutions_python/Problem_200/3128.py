t=input()
m=1
while m<=t:
	n=input()
	k=list(str(n))
	ind=-1
	for i in xrange(len(k)):
		if i!=len(k)-1:
			if k[i]>k[i+1]:
				if i==0:
					k[i]=str(int(k[i])-1)
					ind=1
					
				else:
					while i!=0 and k[i-1]==k[i]:
						i-=1
					k[i]=str(int(k[i])-1)
					ind=i+1
				break
	if ind!=-1:
		while ind<len(k):
			k[ind]='9'
			ind+=1
	print "Case #"+str(m)+":",int("".join(k))
	m+=1
	