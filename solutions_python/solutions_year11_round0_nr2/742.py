t=int(raw_input())
cas=0
while t:
	cas+=1
	t-=1
	d={}
	e={}
	l=[x for x in raw_input().split()]
	i=0;
	ans=[]
	while i<len(l):
		j=int(l[i]);
		i+=1;
#		print j
		for k in range(0,j):
			d[l[i][0]+l[i][1]]=l[i][2];
			d[l[i][1]+l[i][0]]=l[i][2];
			i+=1;
		j=int(l[i]);
#		print j
		i+=1;
		for k in range(0,j):
			e[l[i][0]+l[i][1]]=1;
			e[l[i][1]+l[i][0]]=1;
			i+=1;
		j=int(l[i]);
#		print j

		i+=1;
		ans.append(l[i][0]);
		for k in range(1,j):
			ans.append(l[i][k]);
			while True:
#				print ans
				if len(ans)>1:
					last=ans.pop();
					last2=ans.pop();
				else:
					last='';
					break;
				if(d.has_key(last+last2)):
					ans.append(d[last+last2]);
				elif(d.has_key(last2+last)):
					ans.append(d[last2+last]);
				else:
					ans.append(last2);
					ans.append(last);
					break;
			if len(ans)>1:
				last=ans[-1];
				for w in range(0,len(ans)-1):
					if e.has_key(ans[w]+last):
						ans=[]
						break
					elif e.has_key(last+ans[w]):
						ans=[]
						break
		s='Case #%d: ['%cas
		if(len(ans)!=0):
			s+=ans[0]
			for m in range(1,len(ans)):
				s+=', '+ans[m]
		s+=']'
		i+=1
		print s
		break

					

