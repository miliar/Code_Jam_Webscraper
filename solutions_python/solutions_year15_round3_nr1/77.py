f=open('A-large.in','r')
f1=open('out.txt','w')
casenum=int(f.readline().replace('\n',''))
for i in range(0,casenum):
	line=f.readline().replace('\n','').split(' ')
	r=int(line[0])
	c=int(line[1])
	w=int(line[2])
	res=0
	find1=c/w
	find2=find1*(r-1)
	if c%w==0:
		res=find2+c/w+w-1
	else:
		res=find2+c/w+w
	f1.write('Case #'+str(i+1)+': '+str(res)+'\n')
f.close()
f1.close()