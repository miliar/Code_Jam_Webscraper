import sys
T=int(sys.stdin.readline().strip())
for t in range(1,T+1):
	nums=sys.stdin.readline().strip().split(' ')
	N=int(nums[0])
	res=0
	o=[]
	b=[]
	
	for i in range(N):
		if nums[2*i+1]=='O':
			o.append((i,int(nums[2*i+2])))
		else:
			b.append((i,int(nums[2*i+2])))

	i,j=0,0
	po,pb=1,1
	while i<len(o) and j<len(b):
		if o[i][0]<b[j][0]:
			if po==o[i][1]:
				i+=1
			elif po>o[i][1]:
				po-=1
			else:
				po+=1
			if pb>b[j][1]:
				pb-=1
			elif pb<b[j][1]:
				pb+=1
		else:
			if pb==b[j][1]:
				j+=1
			elif pb>b[j][1]:
				pb-=1
			else:
				pb+=1
			if po<o[i][1]:
				po+=1
			elif po>o[i][1]:
				po-=1
		res+=1
	while i<len(o):
		res+=(abs(po-o[i][1])+1)
		po=o[i][1]
		i+=1
	while j<len(b):
		res+=(abs(pb-b[j][1])+1)
		pb=b[j][1]
		j+=1
	print "Case #%d: %d" % (t, res)


		