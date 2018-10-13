import copy
t=int(raw_input())
for f in range(0,t):
	n=int(raw_input())
	nau=raw_input().split()
	k=raw_input().split()
	naumi=list()
	ken=list()
	for i in range(0,n):
		a=nau[i]
		b=k[i]
		naumi.append(float(a))
		ken.append(float(b))
	naumi.sort()
	ken.sort()
	naumi1=copy.copy(naumi)
	ken1=copy.copy(ken)
	
	ken_lowest=ken[0]
	i=0
	#while (i<n):
	#	if (ken_lowest>naumi[i]):
	#		#print i
	#		i+=1
	#	else:
	#		break
	flag=0
	for i in range(0,n):
		for j in range (0,n):
			if(naumi[j]>ken[i]):
				flag+=1
				naumi[j]=0
				break		
	
		
	deceit=flag
	#print 'Deciet'+deceit
	i=0
	j=0
	flag=0
	for i in range(0,n):
		for j in range (0,n):
			if(ken1[j]>naumi1[i]):
				flag+=1
				ken1[j]=0
				break		
	war=n-flag
	print 'Case #'+str(f+1)+': '+str(deceit)+' '+str(war) 
	
	

	