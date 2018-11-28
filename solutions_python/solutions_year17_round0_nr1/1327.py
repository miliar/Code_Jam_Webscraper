li=[]

def flip(k, i):
	for j in xrange(k):
		li[j+i]*=-1
	return

t=int(raw_input())

for i in xrange(t):
	data1=raw_input().strip().split()
	k=int(data1[1])
	data=data1[0]
	checklist=[1]*len(data)
	li=[]
	
	for char in data:
		if char=='+':
			li.append(1)
		elif char=='-':
			li.append(-1)
	j=0
	flag=0
	count=0
	while(li!=checklist):
		if(j>=len(li)-k+1):
			print "Case #"+str(i+1)+ ": IMPOSSIBLE"
			flag=1
			break
		if li[j]==-1:
			count+=1
			flip(k, j)
		j+=1
	if flag==0:
		print "Case #"+ str(i+1)+": "+str(count)
