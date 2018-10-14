t=input()
for j in range(1,t+1):
	x=map(str,raw_input().split())
	foo = list(x[0])
	# print "".join(foo),
	k = int(x[1])
	i=0
	res=0	# answer
	while(i < len(foo)):
		if(foo[i] == "+"):
			i+=1
		elif(i+k-1<len(foo)):
			m=i
			while(m<=i+k-1):
				if(foo[m]=='+'):
					foo[m]='-'
				else:
					foo[m]='+'
				m+=1
			i=i+1
			res+=1
		else:
			res=-1
			break
	# print res
	# print k,
	if(res==-1):
		print "Case #"+str(j)+": IMPOSSIBLE"
	else:
		print "Case #"+str(j)+": "+str(res)
