a=input()
for i in range(a):
	count=0
	b=raw_input()
	d=list(b)
	for j in range(-1,-len(d)-1,-1):
		if(j-1>=-len(d)):
			if int(d[j]<d[j-1]):
				for m in range(-j):
					d[j+m]="9"
				d[j-1]=str(int(d[j-1])-1)
	if int(d[0])==0:
		d.pop(0)
	al=""
	for l in range(len(d)):
		al+=d[l]
	print "Case #%d: %s"%(i+1,al)
	
