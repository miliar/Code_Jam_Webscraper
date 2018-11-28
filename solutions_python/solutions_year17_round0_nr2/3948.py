t= input()
#t=1
t1=0
while t1<t:
	n=raw_input()
	#n="998"
	t1=t1+1
	nl=list(n)
	nl = map(int, nl)
	#print nl
	flag_first=False
	for i in range(len(nl)-1):
		if nl[i]>nl[i+1]:
			

			
				
			j=i
			if j>0 and nl[j]== nl[j-1]:
				#print j
				while j>0 and nl[j]== nl[j-1]:
					if nl[j]!=1:
						nl[j]=nl[j]-1
					else:
						nl[j]=9
					
					if j-1==0:
						flag_first=True
					j=j-1

				#print j
				

				nl[j]=nl[j]-1
				if flag_first:
					i=j

			else:
				nl[i]=nl[i]-1

				
			while i<len(nl)-1:
				i=i+1
				nl[i]=9
		else:
			i=i+1

	#print nl
	op1=int(''.join(map(str,nl)))
	print "Case #%d: %d"%(t1,op1)
	