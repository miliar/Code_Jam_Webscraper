t=input()
for a in range(t):
	n=raw_input()
	n=list(n)
	le=len(n)
	small=int(n[le-1])
	j=len(n)-2
	anchor=len(n)
	while(j>=0):
		if(int(n[j])<small):
			small=int(n[j])
		elif(int(n[j])>small):
			small=int(n[j])-1
			n[j]=str(small)
			for k in range(j+1,anchor):
				n[k]='9'
			anchor=j+1;
		j-=1
	if(n[0]=='0'):
		print "Case #"+str(a+1)+": "+"".join(n[1:])
	else:
		print "Case #"+str(a+1)+": "+"".join(n)