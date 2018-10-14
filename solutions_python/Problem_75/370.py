import psyco
psyco.full()
t=input()
i=1
while i<=t:
	str=raw_input()
	inp=str.split()
	j=1
	l=int(inp[0])+j
	com={}
	while j<l:
		test=inp[j][0:2]
		if test not in com:
			com[test]=inp[j][2]
		j+=1
	l=int(inp[j])+j+1
	j+=1
	opo=[]
	while j<l:
		opo.append(inp[j])
		j+=1
	j+=1;
	string = inp[j]
	ans=[]
	j=0
	l=len(string)
	p=0
	while j<l:
		flag=0
		if flag==0:
			if p>0:
				if string[j]+ans[p-1] in com:
					ans[p-1]=com[string[j]+ans[p-1]]
				elif ans[p-1]+string[j] in com:
					ans[p-1]=com[ans[p-1]+string[j]]
				else:
					ans.append(string[j])
					p+=1
			else:
				ans.append(string[j])
				p+=1
		k=0
		while k<(p-1):
			if ans[p-1]+ans[k] in opo:
				ans=[]
				p=0
				flag=1
				break
			if ans[k]+ans[p-1] in opo:
				ans=[]
				p=0
				flag=1
				break
			k+=1
		j+=1
#		print ans
	print "Case #"+repr(i)+":",
	j=1
	l=len(ans)
	if l>0:
		if l>1:
			print "["+ans[0]+",",
		else:
			print "["+ans[0]+"]"
	else:
		print "[]"
	while j<l:
		if j!=l-1:
			print ans[j]+",",
		else:
			print ans[j]+"]"
		j+=1
#	print l
#	print ans[len(ans)-1]+"]"
	i+=1
