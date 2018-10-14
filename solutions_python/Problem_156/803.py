T=int(raw_input())
t=T
while t:
	D=int(raw_input())
	d=map(int,raw_input().split())

	ans=max(d)
	tmp=sum(d)
	special=0
	case9=0
	d2=d+[]
	if ans==9:	
		for ind,i in enumerate(d2):
			if i==ans:
				d2[ind]=0
				break
		d2m=max(d2)
		if d2m==6:
			for ind,i in enumerate(d2):
				if i==d2m:
					d2[ind]=0
					break
		if max(d2)>=4:
			case9=0
		else:
			case9=1
	for ind,val in enumerate(d):
		if val==ans:
			if not case9:
				special+=1
				d[ind]=int((val+1)/2)
				d.append(val/2)
				#print d
				break
			else:
				special+=2
				d[ind]=int(val/3)
				d.append(3)
				d.append(3)
				#print d
				break
	ans2=max(d)+special
	#print 'Ans: '+str(ans)+'  Ans2: '+str(ans2)
	while ans2<tmp:
		if ans2<ans:
			ans=ans2
		m=max(d)
		#print 'Its Smaller'
		for ind,val in enumerate(d):
			if val==m:
				special+=1
				d[ind]=int((val+1)/2)
				d.append(int(val/2))
				#print d
				break
		ans2=max(d)+special
		#print 'Ans: '+str(ans)+'  Ans2: '+str(ans2)
	if ans2<ans:
		print 'Case #'+str(T-t+1)+': '+str(ans2)
	else:
		print 'Case #'+str(T-t+1)+': '+str(ans)
	t-=1